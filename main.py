from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

try:
        logger.info("Data Ingestion stage")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info("Data Ingestion stagecompleted successfully.")
except Exception as e:
        logger.exception(e)
        raise e