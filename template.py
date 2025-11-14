import os
import sys
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s]: %(levelname)s: %(message)s"
)

list_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/commons/__init__.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/__init__.py",
    "src/logger/logger.py",
    "src/exception/__init__.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    ".env"
    "experiment/experiments.ipynb",
]


def create_project_structure():
    for file_path in list_files:
        filepath = Path(file_path)
        filedir, filename = os.path.split(filepath)

        # Create directory if not exists
        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory: {filedir}")

        # Create file if not exists or is empty
        if not filepath.exists() or filepath.stat().st_size == 0:
            with open(filepath, "w") as f:
                pass
            logging.info(f"Creating empty file: {filepath}")


if __name__ == "__main__":
    logging.info("Creating project structure...")
    create_project_structure()
    logging.info("Project structure created successfully!")
