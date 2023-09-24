import os
from src_.logger import logging
from src_.components.data_ingestion import DataIngestion
from src_.components.data_transformation import DataTransformation
import dtale

class ShowTable:
    def __init__(self, database_path, database_name) -> None:
        self.database_path = database_path
        self.file = os.path.join(self.database_path, database_name)
        
        if not os.path.exists(self.file):
            logging.error(f"Database {database_name} not found in {database_path}")
            return
        
        self.data_ingestion = DataIngestion(self.file)
        self.compounds = self.data_ingestion.convert_db_to_list()

        self.transformer = DataTransformation(self.compounds)
        self.df = self.transformer.create_df() # Create dataframe

        self.dtale_instance = None

    def open_in_dtale(self):
        if self.df is not None:
            # Create a D-Tale instance and pass the DataFrame to it
            self.dtale_instance = dtale.show(self.df, host='0.0.0.0', port=40000, subprocess = False)
            # Provide the URL for accessing the D-Tale web interface
            logging.info(f"Opened D-Tale instance at {self.dtale_instance._url}")
            return self.dtale_instance._url

    def close_dtale(self):
        if self.dtale_instance is not None:
            # Stop the D-Tale instance when done
            self.dtale_instance.kill()
            logging.info("Closed D-Tale instance")
            return

    @staticmethod
    def prompt_for_database_name():
        return input("Please enter the name of the database: ")

if __name__ == "__main__":
    database_path = "artifacts/db_files"
    database_name = ShowTable.prompt_for_database_name()
    show_table = ShowTable(database_path, database_name)
    print(show_table.open_in_dtale())

