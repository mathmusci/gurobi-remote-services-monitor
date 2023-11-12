from textual.app import App

from grb_rs_monitor.components.screens import (Help, GurobiComputeServerJobMonitor)

class MonitorApp(App):
    __name__ = "MonitorApp"

    CSS_PATH = "styles/app.css"
    TITLE = "Gurobi Compute Server Jobs Monitor"
    SCREENS = {"help": Help} 

    def __init__(self, grb_rs_url, grb_rs_client_password, grb_rs_admin_password, mock):
        """Instantiate Gurobi Compute Server Jobs Monitor.
        """
        super().__init__()
        self.grb_rs_url = grb_rs_url
        self.grb_rs_client_password = grb_rs_client_password
        self.grb_rs_admin_password = grb_rs_admin_password
        self.mock_mode = mock

    def on_mount(self) -> None:
        """Set up the application on startup."""
        grb_rs_auth = {"grb_rs_url": self.grb_rs_url,
                       "grb_rs_client_password": self.grb_rs_client_password,
                       "grb_rs_admin_password": self.grb_rs_admin_password}
        self.push_screen(
            GurobiComputeServerJobMonitor(grb_rs_auth=grb_rs_auth, mock=self.mock_mode)
        )
