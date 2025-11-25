import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.loggers import logger
from src.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split(self):
        logger.info("Reading dataset for train-test split...")
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data, test_size=0.2, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Train-Test Split Completed")
        logger.info(f"Train Shape: {train.shape}")
        logger.info(f"Test Shape: {test.shape}")

        return True
