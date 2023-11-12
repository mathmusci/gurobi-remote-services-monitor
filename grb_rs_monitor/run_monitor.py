import click

from grb_rs_monitor.components.app import MonitorApp

@click.command()
@click.option("--url", help="The URL (including the port number) at which the Gurobi Remote Services Agent is available.")
@click.option("--password", "-p", default=None, help="Gurobi Remote Services client password.")
@click.option("--mock", "-m", is_flag=True, default=False, help="Use mock run mode.")
def main(url, password, mock):
    """Run the Gurobi Remote Services Job Monitor app using the command line arguments.
    """
    app = MonitorApp(url, password, None, mock)
    app.run()

if __name__ == '__main__':
    main()
