import os
from src.logger import logging
from ase.db import connect
from src.utils import save_pickle


class DataIngestion:
    def __init__(self, database_path : str) -> None:
        """ Initialize DataIngestion class
        Args:
            database_path (str): path to database file
        Returns:
            None
        """
        self.database_path = database_path
        self.root_data_path = os.path.join("artifacts", "data")
        self.raw_list_path = os.path.join(self.root_data_path, "raw_data.pkl")

    logging.info("Entering Data Ingestion")

    def convert_database_to_list(self) -> list:
        """Converts the databse to atoms and saves it
        Args:
            None
        Returns:
            pd.DataFrame: dataframe of the database
        """
        try:
            database = connect(self.database_path)
        except Exception as e:
            logging.error(f"Error connecting to database: {e}")
            raise e
        else:
            logging.info("Connected to database")
            compounds = database.select()
            logging.info("Selected all compounds from database")
            compounds = [compound for compound in compounds]
            logging.info("Stored all compounds in list")

            # Check if the directory exists
            if not os.path.exists(self.root_data_path):
                os.makedirs(self.root_data_path)
                logging.info(f"Created directory {self.root_data_path}")
            save_pickle(compounds, self.raw_list_path)
            return compounds
        
if __name__ == "__main__":
    database_path = "/Users/archismanchakraborti/Desktop/python_files/HRI_Research_Work/Compound_filtering/c2db-2021-06-24.db"
    data_ingestion = DataIngestion(database_path)
    compounds = data_ingestion.convert_database_to_list()
    print(compounds)
