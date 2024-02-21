import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    # .gitkeep hidden cause empty folder is not uploaded to github
    f"src/{project_name}/__init__.py",
    # will be installed as local package
    f"src/{project_name}/componets/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    # all utilities will be written inside this file
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    # will contain all model related paremeters
    "app.py",
    "main.py",
    "Dockerfile",
    # to build docker image of our source code
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
    # will conatin all notebook experiments
]

for filepath in list_of_files:
    filepath = Path(filepath) # will change the file path format according the the os being used.
    filedir, filename = os.path.split(filepath) 

    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # will make the folder and exit_ok condition checks wether the foder is already available
        logging.info(f"Creating directory:{filedir} for the {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # we are checking file size so we do not replace a file conatining some code
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
