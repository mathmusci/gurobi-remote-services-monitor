# Gurobi Compute Server Jobs Monitor
## Introduction
This tool is a terminal user interface (TUI) that allows one to access information about Gurobi Remote Services cluster nodes and jobs. It may be viewed as a simplified version of the browser-based [Compute Server's Cluster Manager](https://www.gurobi.com/documentation/10.0/remoteservices/remoteservices.html).

## What is displayed
The main screen provides summary information about 
* the cluster and cluster nodes (upper pane);
* jobs as obtained from Compute Server (left pane);
* individual job summary and statistics (right pane).

## Key bindings
### Main screen
* **Switch between job views** :: When a job is selected press `S` to switch between `json` and human-friendly view of job summary (right pane).

### Help screen
* **View help screen** :: When in the main screen, press `H` to see help screen.
* **Switch to main screen** :: When in the help screen, press `Q`, `E`, `Esc`, `Space` or `Enter` to switch back to the main screen.
* **Pause job updates** :: When in the main screen, press `P` to pause updates from Compute Server. Use `R` to resume the updates.
* **Resume job updates** :: When in the main screen, press `R` to pause updates from Compute Server. Use `P` to pause the updates.

## Authors
This tool is an open source project available under the [MIT License](https://github.com/mathmusci/gurobi-remote-services-monitor/blob/main/LICENSE). Its [code is available on Github](`https://github.com/mathmusci/gurobi-remote-services-monitor`). The initial version has been developed by Andrei Bejan, National Grid ESO and Wipro, UK.