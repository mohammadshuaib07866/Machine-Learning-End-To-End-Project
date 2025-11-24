from src.config.configuration import ConfigurationManager
from src.entity.config_entity import DataIngestionconfig
from urllib.request import urlretrieve
from src.loggers import logger
import zipfile


import os

class DataIngestion:
    def __init__(self, config: DataIngestionconfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file,
            )
            logger.info(f"{filename} download with following info:\n {headers}")
        else:
            logger.info(f"File already exists")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)