from Asian_African_Elephants_Classification import logger
from Asian_African_Elephants_Classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Asian_African_Elephants_Classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from Asian_African_Elephants_Classification.pipeline.stage_03_training import ModelTrainingPipeline
from Asian_African_Elephants_Classification.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME= "Data Ingestion Stage"                                               #1

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= "Prepare Base Model Stage"                                           #2

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion =PrepareBaseModelTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"                                                          #3

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME ="Evaluation Stage"                                                   #4


try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e