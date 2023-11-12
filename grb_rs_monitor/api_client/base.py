from abc import ABC, abstractmethod

class TimeDelay():
    def wait_until_server_becomes_available(self):
        """Check whether Gurobi Compute Server is online, and if not - wait until it comes up online.
        """
        sleep_interval_sec = 10
        time_elapsed = 0
        while not self.is_online:
            time.sleep(sleep_interval_sec)
            time_elapsed += sleep_interval_sec
            if time_elapsed > 60 * 5:
                logging.info("Spent another 5 minutes waiting for Gurobi Compute Server to come up online.")

class GurobiComputeServerClientBase(ABC, TimeDelay):
	"""Gurobi Compute Server client base class - all clients (real and mock ones) should be based on this class.
	"""
	# mapping between the numeric constants that represent Gurobi job statuses mapped into their string representation
	NUM2STATUS = {
	        0: "UNKNOWN",
	        1: "QUEUED",
	        2: "RUNNING",
	        3: "ABORTED",
	        4: "FAILED",
	        5: "COMPLETED",
	        6: "REJECTED",
	        7: "DISCONNECTED",
	        8: "IDLETIMEOUT"
	    }

	def __init__(self, grb_rs_url: str, grb_rs_client_password: str, grb_rs_admin_password: str=None) -> None:
		"""Instantiate a client object.
		Args:
			grb_rs_url: URL at which Gurobi Remote Services Agent/API is available.
			grb_rs_client_password: user password
			grb_rs_admin_password: admin password (optional)
		Returns:
			None
		"""
		pass
	
	def __enter__(self):
		pass

	def __exit__(self, type, value, traceback):
		pass

	@property
	@abstractmethod
	def joblimit(self) -> int:
		"""Query Gurobi Compute Server, fetch and return its current JOBLIMIT value.
		"""
		pass

	@joblimit.setter
	def joblimit(self, x: int):
		"""Setter method for the attribute joblimit.
		"""
		self._joblimit_setter(x)

	@abstractmethod
	def _joblimit_setter(self, job_limit: int):
		"""Set Gurobi Compute Server's JOBLIMIT to a predefined value.
		"""
		pass

	@property
	@abstractmethod
	def is_online(self) -> bool:
		"""Poll Gurobi Compute Server to check whether it is online.
		Return True if CS is online and False otherwise.
		"""
		pass

	@property
	@abstractmethod
	def is_idle(self, queued: bool=True) -> bool:
		"""Check whether Gurobi Compute Server is idle (return True) or not (return False).
		We consider the server to be idle when there are no active or pending jobs.
		"""
		pass

	@abstractmethod
	def get_jobs(self, running: bool=True, queued: bool=True, aggregate: bool=False, recent: bool=True) -> dict:
		"""Get Compute Server jobs in a customisable way by specifying the job category/categories of interest.
		"""
		pass

	@abstractmethod
	def get_nodes(self) -> dict:
		"""Get cluster and nodes information.
		"""
		pass

	@property
	@abstractmethod
	def number_of_running_jobs(self) -> int:
		"""Get the number of running jobs.
		"""
		pass
