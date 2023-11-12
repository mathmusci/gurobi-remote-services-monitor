from collections import defaultdict
import sys
import json
import datetime
import gurobipy

from rich.traceback import Traceback
from rich.syntax import Syntax
from rich.rule import Rule
from rich.table import Table
from rich.console import Group

from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Container, Vertical
from textual.binding import Binding
from textual.widgets import Static, Footer

from grb_rs_monitor.components.widgets import AppHeader, JobsTree, help_content
from grb_rs_monitor.api_client.grb_rs_client import GurobiComputeServerClient, GurobiComputeServerClientMock 


class Help(Screen):
    """The help screen for the application.
    """

    BINDINGS = [("escape,space,q,e,enter", "pop_screen", "Close")]

    def compose(self) -> ComposeResult:
        """Compose the contents of the help screen.

        Returns:
            ComposeResult: The result of composing the help screen.
        """
        yield help_content


JOB_CHAR = '▰'
VACANT_CHAR = '▱'

def generate_workload_indicator(buffer_size, jobs):
    """Generate workload indicator string.
    """
    if jobs <= buffer_size:
        return JOB_CHAR * jobs + VACANT_CHAR * (buffer_size - jobs)
    else:
        sys.exit("Check the number of jobs and buffer size values!")


class GurobiComputeServerJobMonitor(Screen):
    TITLE = "Gurobi Compute Server Jobs Monitor"
    BINDINGS = [
        Binding(key="s", action="switch_job_view", description="Switch between job views"),
        Binding(key="p", action="pause", description="Pause"),
        Binding(key="r", action="resume", description="Resume"),
        Binding(key="h", action="push_screen('help')", description="Help"),
        Binding(key="q", action="quit", description="Quit")
    ]

    def __init__(self, grb_rs_auth={}, mock=False):
        """Instantiate either an actual (mock=False) or a mock client (mock=True).
        """
        super().__init__()
        self.pause_updates = False
        APIClient = GurobiComputeServerClient if not mock else GurobiComputeServerClientMock
        self.grb_rs_client = APIClient(**grb_rs_auth)
        self.jobs = []

    def compose(self) -> ComposeResult:
        """Compose application's layout and id the components.
        """
        yield AppHeader()
        yield Container(
            Vertical(Static("Cluster and cluster nodes", id="cluster-and-nodes-header"),
                     Static("", expand=True, id="cluster-and-nodes-content"),
                     id="cluster-and-nodes"),
            JobsTree("Jobs", id="tree-view"),
            Vertical(Static("Job details", id="job-header"),
                     Static("", expand=True, id="job-details"), id="job-view"),
            id="app-grid"
        )
        yield Footer()

    def _update_jobs(self):
        """Update the jobs tree.
        """
        if not self.pause_updates:
            tree = self.query_one(JobsTree)
            tree.clear()
            d = defaultdict(list)
            self.jobs = self.grb_rs_client.get_jobs()
            for job in self.jobs:
                d[self.grb_rs_client.NUM2STATUS[job["status"]]].append(job["id"])
            tree.root.expand()
            statuses = {status: tree.root.add(status, expand=True) for status in d}
            for status in statuses:
                for job_id in d[status]:
                    statuses[status].add_leaf(job_id)

    def _update_cluster_and_nodes_pane(self):
        """Update the cluster and nodes pane.
        """
        if not self.pause_updates:
            cluster_nodes = self.grb_rs_client.get_nodes()
            cluster_node_tables = self._build_cluster_nodes_tables(cluster_nodes)
            content = Group(*cluster_node_tables)

            cluster_and_nodes_view = self.query_one("#cluster-and-nodes-content")
            cluster_and_nodes_view.update(content)

    def _get_job_by_id(self, job_id):
        """Find a job by its ID.
        """
        return next(job for job in self.jobs if job["id"] == job_id)

    def on_mount(self) -> None:
        """Set intervals and callbacks upon mounting.
        """
        self.set_interval(0.5, self._update_jobs)
        self.set_interval(0.25, self._update_cluster_and_nodes_pane)

    def on_tree_node_selected(self, event: JobsTree.NodeSelected):
        """Describe what happens when a tree node (i.e. optimisation job) is selected.
        """
        event.stop()
        tree = self.query_one(JobsTree)
        tree.selected_job_id = event.node._label
        self._update_job_details(tree.selected_job_id)

    def _build_cluster_nodes_tables(self, nodes):
        """Build Gurobi Compute cluster nodes tables.
        """
        tables = []
        fmt = "%Y-%m-%dT%H:%M:%SZ"
        NODE_TYPE = {1: "Compute Server", 2: "Worker"}
        NODE_STATUS = {1: "ALIVE", 2: "FAILED", 3: "JOINING", 4: "LEAVING", 5: "DEGRADED"}
        LICENSE = {0: "NA", 1: "valid", 2: "invalid", 3: "expired"}
        PROCESSING = {1: "ACCEPTING", 2: "DRAINING", 3: "STOPPED"}

        for node_obj in nodes:
            node = node_obj if isinstance(node_obj, dict) else node_obj.to_dict()
            node_type = NODE_TYPE[node["type"]] if "type" in node else "type unknown"
            node_status = NODE_STATUS[node["status"]] if "status" in node else "status unknown"
            license = LICENSE[node["license"]] if "license" in node else "license info unavailable"
            job_limit = str(node["job_limit"]) if "job_limit" in node else "NA"
            version = node["version"] if "version" in node else "NA"
            processing = PROCESSING[node["processing"]] if "job_limit" in node else "NA"
            address = node["address"] if "address" in node else "NA"

            nb_running_jobs = str(node["metrics"]["nb_running_jobs"]
                                  ) if "metrics" in node and "nb_running_jobs" in node["metrics"] else "NA"
            nb_queued_jobs = str(node["metrics"]["nb_queued_jobs"]) if "metrics" in node and "nb_queued_jobs" in node["metrics"] else "NA"
            nb_recent_jobs = str(node["metrics"]["nb_recent_jobs"]) if "metrics" in node and "nb_recent_jobs" in node["metrics"] else "NA"
            processed_job_counter = str(node["metrics"]["processed_job_counter"]
                                        ) if "metrics" in node and "processed_job_counter" in node["metrics"] else "NA"
            idle_time = str(node["metrics"]["idle_time"]) if "metrics" in node and "idle_time" in node["metrics"] else "NA"
            memory = str(node["metrics"]["memory"]) + "%" if "metrics" in node and "memory" in node["metrics"] else "NA"
            cpu = str(node["metrics"]["cpu"]) + "%" if "metrics" in node and "cpu" in node["metrics"] else "NA"

            if "started_at" in node:
                node_start_time = datetime.datetime.fromtimestamp(node["started_at"] / 1e3).strftime(fmt)
            else:
                node_start_time = "unknown time"

            table = Table(title=f"{node_type} {node['id']} on host {address}",
                          box=None, expand=True, header_style="yellow bold")
            table.add_column("version", justify="left", style="white", no_wrap=True)
            table.add_column("status", justify="left", style="white", no_wrap=True)
            table.add_column("processing", justify="left", style="white", no_wrap=True)
            table.add_column("job limit", justify="left", style="white", no_wrap=True)
            table.add_column("license", justify="left", style="white", no_wrap=True)
            table.add_column("started at", justify="left", style="white", no_wrap=True)

            table.add_column("running jobs", justify="left", style="white", no_wrap=True)
            table.add_column("queued jobs", justify="left", style="white", no_wrap=True)
            table.add_column("recent jobs", justify="left", style="white", no_wrap=True)
            table.add_column("processed jobs", justify="left", style="white", no_wrap=True)
            table.add_column("idle time", justify="left", style="white", no_wrap=True)
            table.add_column("memory", justify="left", style="white", no_wrap=True)
            table.add_column("cpu", justify="left", style="white", no_wrap=True)

            table.add_row(version, node_status, processing, job_limit, license, node_start_time,
                          nb_running_jobs, nb_queued_jobs, nb_recent_jobs, processed_job_counter, idle_time, memory, cpu)

            tables.append(table)

        return tables

    def _build_job_summary_tables(self, node_label):
        """Build job summary tables.
        """
        # job_view = self.query_one("#job-details")
        tree = self.query_one(JobsTree)
        try:
            job = self._get_job_by_id(str(node_label))
        except Exception:
            return dict()
        else:
            tables = dict()

            # populate the server/client information table
            table = Table(title="Server/client information", box=None, expand=True)
            table.add_column("Job attribute", justify="right", style="green bold", no_wrap=True)
            table.add_column("Details", justify="left", style="white", no_wrap=False)
            table.add_row("status", tree.NUM2STATUS[job['status']])
            table.add_row("address", job['address'])
            table.add_row("node ID", job['nodeId'])
            table.add_row("job ID", job['id'])
            table.add_row("user",
                          f"user {job['properties']['username']} at host {job['properties']['hostname']} (IP {job['properties']['ip']})")
            table.add_row("API", f"{job['properties']['apitype']} client version {job['properties']['runtime']}")

            tables["server-client"] = table

            # populate the job processing time table
            table = Table(title="Job processing time", box=None, expand=True, header_style="green bold")
            table.add_column("time started", justify="left", style="white", no_wrap=True)
            table.add_column("time ended", justify="left", style="white", no_wrap=True)
            table.add_column("duration (seconds)", justify="left", style="white", no_wrap=True)
            table.add_column("duration (milliseconds)", justify="left", style="white", no_wrap=True)

            if "startedAt" in job:
                started_at = datetime.datetime.fromtimestamp(job["startedAt"] / 1e3)

                fmt = "%Y-%m-%dT%H:%M:%SZ"
                if "endedAt" in job:
                    ended_at = datetime.datetime.fromtimestamp(job["endedAt"] / 1e3)
                    ended_at_as_str = ended_at.strftime(fmt)
                    duration_sec_as_str = str((ended_at - started_at).seconds)
                    duration_mlsec_as_str = str((ended_at - started_at).microseconds / 1000.0)
                else:
                    ended_at_as_str = "NA"
                    duration_sec_as_str = "NA"
                    duration_mlsec_as_str = "NA"

                table.add_row(started_at.strftime(fmt),
                              ended_at_as_str,
                              duration_sec_as_str,
                              duration_mlsec_as_str
                              )
            else:
                started_at = "NA"

            tables['times'] = table

            # populate the model info table
            table = Table(title="Model info", box=None, expand=True, header_style="green bold")
            table.add_column("rows", justify="left", style="white", no_wrap=True)
            table.add_column("columns", justify="left", style="white", no_wrap=True)
            table.add_column("non zeros", justify="left", style="white", no_wrap=True)
            table.add_column("ts", justify="left", style="white", no_wrap=True)

            if "modelInfo" in job:
                rows = job["modelInfo"]["rows"]
                cols = job["modelInfo"]["cols"]
                nonz = job["modelInfo"]["nonz"]
                table.add_row(str(rows),
                              str(cols),
                              f"{nonz} ({round(100*nonz/(rows*cols), 2)}%)",
                              datetime.datetime.fromtimestamp(job["modelInfo"]["ts"] / 1e3).strftime(fmt)
                              )
            else:
                table.add_row("NA", "NA", "NA", "NA")

            tables["model-info"] = table

            # populate the MIP info table
            table = Table(title="MIP info", box=None, expand=True, header_style="green bold")
            table.add_column("best objective", justify="left", style="white", no_wrap=True)
            table.add_column("best objective bound", justify="left", style="white", no_wrap=True)
            table.add_column("explored node count", justify="left", style="white", no_wrap=True)
            table.add_column("unexplored node count", justify="left", style="white", no_wrap=True)
            table.add_column("feasible solution count", justify="left", style="white", no_wrap=True)
            table.add_column("cutting planes applied", justify="left", style="white", no_wrap=True)

            objbst = str(job["mipInfo"]["objbst"]) if "mipInfo" in job and "objbst" in job["mipInfo"] else "NA"
            objbnd = str(job["mipInfo"]["objbnd"]) if "mipInfo" in job and "objbnd" in job["mipInfo"] else "NA"
            nodcnt = str(job["mipInfo"]["nodcnt"]) if "mipInfo" in job and "nodcnt" in job["mipInfo"] else "NA"
            nodlft = str(job["mipInfo"]["nodlft"]) if "mipInfo" in job and "nodlft" in job["mipInfo"] else "NA"
            solcnt = str(job["mipInfo"]["solcnt"]) if "mipInfo" in job and "solcnt" in job["mipInfo"] else "NA"
            cutcnt = str(job["mipInfo"]["cutcnt"]) if "mipInfo" in job and "cutcnt" in job["mipInfo"] else "NA"

            table.add_row(objbst, objbnd, nodcnt, nodlft, solcnt, cutcnt)

            tables["mip-info"] = table

            # optimisation status
            grb_status_codes_class = gurobipy.StatusConstClass
            opt_status_codes = {grb_status_codes_class.__dict__[k]: k for k in grb_status_codes_class.__dict__.keys()
                                if k[0] >= "A" and k[0] <= "Z"}

            table = Table(title="Optimisation status", box=None, expand=True)
            table.add_column(" " * len("Job attribute"), justify="right", style="green bold", no_wrap=True)
            table.add_column("Details", justify="left", style="white", no_wrap=False)

            status = opt_status_codes[job["optimizationStatus"]["status"]] if "optimizationStatus" in job \
                and "status" in job["optimizationStatus"] \
                else "NA"
            error = str(job["optimizationStatus"]["error"]) if "optimizationStatus" in job \
                and "error" in job["optimizationStatus"] else "NA"
            errormsg = str(job["optimizationStatus"]["errormsg"]
                           ) if "optimizationStatus" in job and "errormsg" in job["optimizationStatus"] else "NA" + " " * 58
            table.add_row("optimisation status", status)
            table.add_row("error", error)
            table.add_row("error message", errormsg)

            tables["optimisation-status"] = table

            return tables

    def _update_job_details(self, node_label):
        """Update job details.
        """
        job_view = self.query_one("#job-details")
        tree = self.query_one(JobsTree)

        try:
            job_python = self._get_job_by_id(str(node_label))
            if tree.job_view == 'json':
                job_json = json.dumps(job_python, indent=4)
                content = Syntax(job_json, "json",
                                 theme="rrt",
                                 line_numbers=True,
                                 word_wrap=False,
                                 indent_guides=True)
            if tree.job_view == "report":
                tables = self._build_job_summary_tables(str(node_label))
                content = Group(tables["server-client"],
                                Rule(characters=" ", style="white"),
                                Rule(characters="-", style="white"),
                                tables["times"],
                                Rule(characters=" ", style="white"),
                                Rule(characters="-", style="white"),
                                tables["model-info"],
                                Rule(characters=" ", style="white"),
                                Rule(characters="-", style="white"),
                                tables["mip-info"],
                                Rule(characters=" ", style="white"),
                                Rule(characters="-", style="white"),
                                tables["optimisation-status"],
                                Rule(characters=" ", style="white"),
                                Rule(characters="-", style="white")
                                )
        except Exception:
            job_view.update(Traceback(theme="github-dark", width=None))
            job_view.sub_title = "ERROR"
        else:
            job_view.update(content)
            self.query_one("#job-view").scroll_home(animate=False)

    def action_switch_job_view(self):
        """Update job details view type when `S` is pressed.
        """
        tree = self.query_one(JobsTree)
        conversion_dict = {"json": "report", "report": "json"}
        tree.job_view = conversion_dict[tree.job_view]
        self._update_job_details(tree.selected_job_id)

    def action_pause(self):
        """Describe what needs to happen when `P` is pressed.
        """
        self.pause_updates = True
        self.query_one(AppHeader).status = "PAUSED"

    def action_resume(self):
        """Describe what needs to happen when `R` is pressed.
        """
        self.pause_updates = False
        self._update_jobs()
        self.query_one(AppHeader).status = "POLLING"
