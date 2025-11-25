import os
import joblib
import pandas as pd
from sklearn.linear_model import ElasticNet
from src.loggers import logger
from src.config.configuration import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        logger.info("Model training started...")

        train_df = pd.read_csv(self.config.train_data_path)
        test_df = pd.read_csv(self.config.test_data_path)

        X_train = train_df.drop(self.config.target_column, axis=1)
        y_train = train_df[self.config.target_column]

        X_test = test_df.drop(self.config.target_column, axis=1)
        y_test = test_df[self.config.target_column]

        model = ElasticNet(
            alpha=self.config.alpha,
            l1_ratio=self.config.l1_ratio,
            random_state=42
        )
        model.fit(X_train, y_train)

        # IMPORTANT: Create folder
        os.makedirs(self.config.model_path.parent, exist_ok=True)

        joblib.dump(model, self.config.model_path)

        logger.info(f"Model saved at: {self.config.model_path}")
        logger.info("Model training completed!")
