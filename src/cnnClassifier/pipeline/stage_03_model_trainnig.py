from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_training import Training
from cnnClassifier import logger

class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__ == "__main__":
    try:
        logger.info(" stage_03_model_training started ")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(" stage_03_model_training completed ")
    except Exception as e:
        logger.exception(e)
        raise e
