import os 
import sys 
# from src.exception import CustomException
# from src.logger import logging 
import pandas as pd 

from sklearn.model_selection import train_test_split 
from dataclasses import dataclass 

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifact','train.csv')
    test_data_path:str=os.path.join('artifact','test.csv')
    raw_data_path:str=os.path.join('artifact','raw.csv') 

class DataIngestion :
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        # logging.info("Entered The Data Ingestion method or component")
        df = pd.read_csv('D:\\MLProject\\notebook\\data\\stud.csv')
        # logging.info('Read the dataset as dataframe')

        os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok = True)

        df.to_csv(self.ingestion_config.raw_data_path,index = False , header = True)

        # logging.info("Train_Test_Split Initialized")
        train_set,test_set = train_test_split(df,train_size = 0.8,random_state = 42)

        train_set.to_csv(self.ingestion_config.train_data_path,index = False , header = True)
        test_set.to_csv(self.ingestion_config.test_data_path,index = False , header = True)

        # logging.info("Ingestion of the data is Completed")

        return (
            self.ingestion_config.train_data_path,
            self.ingestion_config.test_data_path , 
            )

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()