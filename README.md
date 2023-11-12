# Gurobi Remote Services Monitor

A terminal based Text User Interface (TUI) application that allows one to monitor Gurobi Remote Services (`grb_rs`) and cluster's job queueing and processing activity.

## Requirements and dependency
The Gurobi Remote Services Monitor application (`grb_rs_monitor`) is written in Python using [Textualize](https://www.textualize.io/)'s [`Textual`](https://textual.textualize.io/). Its platform/terminal requirements are therefore as follows:

* Linux (all distributions): All Linux distributions come with a terminal emulator that can run `Textual` apps.

* macOS: The default terminal app is limited to 256 colors. Textualize recommend installing a newer terminal such as `iterm2`, `Kitty`, or `WezTerm`.

* Windows: The new Windows Terminal (PowerShell) runs `Textual` apps.

## How to install
```
pip install grb_rs_monitor
```
## How to run
```
grb_rs_monitor --url $GRB_RS_URL -p $GRB_RS_CLIENT_PSWD
```

If you do not have access to Gurobi Remote Services, it is possible to run the tool in the mock mode using the switch `--m/-m` as follows:
```
grb_rs_monitor --mock --url "mock-url" -p "mock-password"
```