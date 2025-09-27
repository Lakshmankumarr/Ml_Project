import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.exception import CustomException
from src.logger import logging

class DataIngestion:
    def __init__(self, raw_path=r"C:\Users\tmani\Downloads\StudentsPerformance.csv"):
        self.raw_path = raw_path
        self.train_path = os.path.join("artifacts", "train.csv")
        self.test_path = os.path.join("artifacts", "test.csv")
        os.makedirs("artifacts", exist_ok=True)

    def initiate_data_ingestion(self):
        logging.info("Starting data ingestion...")
        try:
            df = pd.read_csv(self.raw_path)
            df.to_csv(os.path.join("artifacts", "data.csv"), index=False, header=True)

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.train_path, index=False)
            test_set.to_csv(self.test_path, index=False)

            logging.info("Data ingestion completed.")
            return self.train_path, self.test_path
        except Exception as e:
            raise CustomException(e, sys)
