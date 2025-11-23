import os
import sys
import json
import yaml
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from src.logger import logger
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError("YAML file is empty")

            logger.info(f"YAML file loaded successfully: {path_to_yaml}")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("Invalid YAML file or empty file")

    except Exception as e:
        logger.error(f"Error reading YAML file: {e}")
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directory created or already exists: {path}")

    except Exception as e:
        logger.error(f"Error creating directories: {e}")
        raise e


@ensure_annotations
def save_json(path: Path, data: dict):
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        logger.info(f"JSON file saved at: {path}")

    except Exception as e:
        logger.error(f"Error saving JSON file: {e}")
        raise e


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    try:
        with open(path) as f:
            content = json.load(f)
        logger.info(f"JSON file loaded from: {path}")
        return ConfigBox(content)

    except Exception as e:
        logger.error(f"Error loading JSON file: {e}")
        raise e


@ensure_annotations
def save_bin(data: Any, path: Path):
    try:
        joblib.dump(value=data, filename=path)
        logger.info(f"Binary file saved at: {path}")

    except Exception as e:
        logger.error(f"Error saving binary file: {e}")
        raise e


@ensure_annotations
def load_bin(path: Path) -> Any:
    try:
        data = joblib.load(path)
        logger.info(f"Binary file loaded from: {path}")
        return data

    except Exception as e:
        logger.error(f"Error loading binary file: {e}")
        raise e
