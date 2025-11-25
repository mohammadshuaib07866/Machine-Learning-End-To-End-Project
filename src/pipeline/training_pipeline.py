from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.config.configuration import ConfigurationManager
from src.components.model_trainer import ModelTrainer
from src.loggers import logger


class DataIngestionTrainingPipeline:
    def initiate_data_ingestion(self):
        config = ConfigurationManager()
        ingestion_config = config.get_data_ingestion_config()

        data_ingestion = DataIngestion(ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


class DataValidationTrainingPipeline:
    def initiate_data_validation(self):
        config = ConfigurationManager()
        validation_config = config.get_data_validation_config()

        data_validation = DataValidation(validation_config)
        status = data_validation.validate_all_columns()
        logger.info(f"Data Validation Status: {status}")


class DataTransformationTrainingPipeline:
    def initiate_data_transformation(self):
        config = ConfigurationManager()
        transformation_config = config.get_data_transformation_config()

        data_transformation = DataTransformation(transformation_config)
        data_transformation.train_test_split()

        logger.info("Data Transformation Completed")


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        logger.info("Initializing Model Trainer Stage...")

        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()

        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()

        logger.info("Model Trainer Stage Completed Successfully!")

