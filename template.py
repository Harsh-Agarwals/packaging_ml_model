import os
from pathlib import Path
import logging
from datetime import datetime

today = datetime.now()
logging_path = os.path.join(os.path.dirname("."), "logs")

if os.path.exists(logging_path):
    print("Logging path exists")
    logging.basicConfig(filename=os.path.join(logging_path, f"log_{today.strftime("%d%m%Y")}"), filemode='w', force=True, format='%(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.warning("==============LOGGER START==============")
    logger.info(f"Current time: {today}")
    logger.warning("-----------------------------\n\n")
else:
    os.makedirs("logs")
    logging.basicConfig(filename=os.path.join(logging_path, f"log_{today.strftime("%d%m%Y")}"), filemode='w', force=True, format='%(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.warning("==============LOGGER START==============")
    logger.info(f"Current time: {today}")
    logger.warning("-----------------------------\n\n")

project_path = "clinical_role"

list_of_files = [
    f"{project_path}/__init__.py",
    f"{project_path}/config/__init__.py",
    f"{project_path}/config/config.py",
    f"{project_path}/datasets/__init__.py",
    f"{project_path}/processing/__init__.py",
    f"{project_path}/pipeline.py",
    f"{project_path}/predict.py",
    f"{project_path}/trained_models/__init__.py",
    f"{project_path}/training_pipeline.py",
    f"{project_path}/research/trials.ipynb",
    "setup.py",
    "mainfest.in",
    "tests/pytest.ini",
    "tests/test_prediction.py"
]

for file in list_of_files:
    dir_name = os.path.dirname(file)
    filename = os.path.basename(file)

    if dir_name != '':
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            logger.warning(f"\nDirectory {dir_name} added.")
    
    file_path = os.path.join(dir_name, filename)
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write('')
        logger.warning(f"{file_path} added to the {dir_name}")

