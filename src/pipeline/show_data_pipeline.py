import numpy as np
import pandas as pd
from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.components.data_ingestion import DataIngestion
import dtale

class ShowTable:
    def __init__(self, database_path) -> None:
        self.database_path = database_path
        self.data_ingestion = DataIngestion(self.database_path)
        self.compounds = self.data_ingestion.convert_database_to_list()

        self.compd_database_path = "artifacts/data/raw_data.pkl"
        self.transformer = DataTransformation(self.compd_database_path)
        self.df = self.transformer.create_df() # Create dataframe

        self.dtale_instance = None

    def open_in_dtale(self):
        if self.df is not None:
            # Create a D-Tale instance and pass the DataFrame to it
            self.dtale_instance = dtale.show(subprocess = False)
            # Provide the URL for accessing the D-Tale web interface
            logging.info(f"Opened D-Tale instance")

    def close_dtale(self):
        if self.dtale_instance is not None:
            # Stop the D-Tale instance when done
            self.dtale_instance.kill()

if __name__ == "__main__":
    database_path = "/Users/archismanchakraborti/Desktop/python_files/HRI_Research_Work/Compound_filtering/c2db-2021-06-24.db"
    show_table = ShowTable(database_path)
    print(show_table.open_in_dtale())
