import os
from src_.logger import logging
from ase.db import connect
from src_.utils import save_pickle


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
        # logging.info("Entering Data Ingestion")

    def convert_db_to_list(self) -> list:
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

            return compounds

        
if __name__ == "__main__":
    # database_path = "/Users/archismanchakraborti/Desktop/python_files/HRI_Research_Work/Data_management/artifacts/db_files/abse3.db"
    # data_ingestion = DataIngestion(database_path)
    # compounds = data_ingestion.convert_db_to_list()
    # print(compounds)
    print(dir(DataIngestion))

