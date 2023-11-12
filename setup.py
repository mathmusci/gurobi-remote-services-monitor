from setuptools import setup, find_packages

setup(
    name="grb-rs-monitor",
    version="0.0.1",
    packages=find_packages(),
    url="",
    license="",
    keywords="gurobi grb gurobipy tui textual python package grb_rs_monitor",
    author="Andrei Bejan",
    author_email="andrei.bejan@nationalgrid.com",
    description="Gurobi Remote Services Monitor",
    include_package_data=True,
    entry_points ={
            "console_scripts": [
                "grb_rs_monitor = grb_rs_monitor.run_monitor:main"
            ]
    },
    classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
    setup_requires=["wheel"], 
    install_requires=["click", 
                      "gurobipy", 
                      "requests", 
                      "six", 
                      "textual"
                    ]
)