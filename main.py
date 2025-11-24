from src.pipeline.training_pipeline import DataIngestionTrainingPipeline
from src.loggers import logger


STAGE_NAME = "Data Ingestion Stage"


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<\n\n =========x")
    except Exception as e:
        raise e