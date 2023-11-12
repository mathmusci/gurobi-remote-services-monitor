import os
from pathlib import Path
from collections import defaultdict
from datetime import datetime
import json

from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Label, Tree
from textual.containers import Horizontal
from textual.reactive import reactive

from rich.markdown import Markdown

directory = str(Path(__file__).resolve().parents[0])

with open(os.path.join(directory, "markdown", "help.md"), "r") as file:
    help_md = file.read()
    help_content = Label(Markdown(help_md))


class AppHeader(Widget):
    """App's header.
    """
    status = reactive("POLLING")
    datetime = reactive(datetime.now().strftime("%c"))

    def compose(self) -> ComposeResult:
        """Compose the app's header.

        Returns:
            ComposeResult: The result of composing the header.
        """
        yield Horizontal(
            Label(Markdown(self.app.title.upper().join([".:: **", "** ::."])),
                  id="app-title"),
            Label(id="status"),
            Label(id="time")
        )

    def _update_dt(self):
        """Register current date and time.
        """
        self.datetime = datetime.now().strftime("%c")

    def on_mount(self):
        """Register a callback on updating date and time upon mounting.
        """
        self.set_interval(1, self._update_dt)

    def watch_status(self, status: str):
        """Watch Gurobi Compute Server's status.
        """
        self.query_one("#status", Label).update(f"Status: {status}")

    def watch_datetime(self, dt: str):
        """Watch current time.
        """
        self.query_one("#time", Label).update(f"Time: {dt}")


class JobsTree(Tree):
    """Tree representation of optimisation jobs fetched from Gurobi Remote Services.
    """
    NUM2STATUS = {0: "UNKNOWN",
                  1: "QUEUED",
                  2: "RUNNING",
                  3: "ABORTED",
                  4: "FAILED",
                  5: "COMPLETED",
                  6: "REJECTED",
                  7: "DISCONNECTED",
                  8: "IDLETIMEOUT"
                  }

    def __init__(self, jobs, name: str = 'JOBS', id=None):
        """Instantiate the job tree.
        """
        super().__init__(name, id=id)
        self.selected_job_id = None
        self.job_view = 'report'  # : could be 'json' or 'report'

        jobs_by_status = defaultdict(list)
        with open("mocks/jobs.json") as f:
            jobs = json.load(f)
            for job in jobs:
                jobs_by_status[self.NUM2STATUS[job["status"]]].append(job["id"])

        self.root.expand()
        statuses = {status: self.root.add(status, expand=True) for status in jobs_by_status}
        for status in statuses:
            for job_id in jobs_by_status[status]:
                statuses[status].add_leaf(job_id)
