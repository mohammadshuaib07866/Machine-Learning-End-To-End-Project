from src.loggers import logger
from src.pipeline.training_pipeline import (
    DataIngestionTrainingPipeline,
    DataValidationTrainingPipeline,
    DataTransformationTrainingPipeline,
)

if __name__ == "__main__":
    try:
        # STAGE 1: INGESTION
        STAGE_NAME = "DATA INGESTION STAGE"
        logger.info(f">>>>>>> {STAGE_NAME} started <<<<<<")
        ingestion = DataIngestionTrainingPipeline()
        ingestion.initiate_data_ingestion()
        logger.info(f">>>>>>> {STAGE_NAME} completed <<<<<<\n")

        # STAGE 2: VALIDATION
        STAGE_NAME = "DATA VALIDATION STAGE"
        logger.info(f">>>>>>> {STAGE_NAME} started <<<<<<")
        validation = DataValidationTrainingPipeline()
        validation.initiate_data_validation()
        logger.info(f">>>>>>> {STAGE_NAME} completed <<<<<<\n")

        # STAGE 3: TRANSFORMATION
        STAGE_NAME = "DATA TRANSFORMATION STAGE"
        logger.info(f">>>>>>> {STAGE_NAME} started <<<<<<")
        transformation = DataTransformationTrainingPipeline()
        transformation.initiate_data_transformation()
        logger.info(f">>>>>>> {STAGE_NAME} completed <<<<<<\n")

    except Exception as e:
        logger.exception(e)
        raise e
