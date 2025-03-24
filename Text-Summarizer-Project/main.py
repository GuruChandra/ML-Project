from textSummarizer.logging import logger
from textSummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage02_data_validation import  DataValidationTrainingPipeline
from textSummarizer.pipeline.stage03_data_tranformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage04_model_trainer import ModelTrainingPipeline
logger.info("Welcome to our custom logging...")

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<< \n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<< \n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_tranformation = DataTransformationTrainingPipeline()
    data_tranformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<< \n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Training Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_tranformation = ModelTrainingPipeline()
    data_tranformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<< \n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e