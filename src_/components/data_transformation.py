from src_.logger import logging
import pandas as pd
import os
import numpy as np
import inspect
from src_.components.data_ingestion import DataIngestion
import periodictable


def element_has_atomic_number_greater_than_50(element_symbol):
    try:
        element = periodictable.elements.symbol(element_symbol.capitalize())
        if element.number > 50:
            return True
        else:
            return False
    except periodictable.core.ElementError:
        return False

def list_has_element_with_atomic_number_greater_than_50(element_list):
    if any(element_has_atomic_number_greater_than_50(element) for element in element_list):
        return True
    return False

class DataTransformation:
    def __init__(self, compounds) -> None:
        try:
            self.compounds = compounds
        except Exception as e:
            logging.error("Error initializing DataTransformation", e)
            raise e
        
        logging.info("Enetering Data Transformation")      
        try:
            self.attributes = [element for element in dir(self.compounds[0]) if not element.startswith('__') and 
                                not element.endswith('__') and not inspect.ismethod(getattr(self.compounds[0], element))] #and
            #   not inspect.isfunction(getattr(self.compounds[0], element))]
        except Exception as e:
            logging.error("Failed to get attributes of compounds")
            raise e

        
    def create_df(self):
        data = np.zeros((len(self.compounds), len(self.attributes)), dtype=object)
        logging.info("Creating dataframe by looping through all compounds and attributes")
        for compd_idx, compound in enumerate(self.compounds):
            for attr_idx, attribute in enumerate(self.attributes):
                if hasattr(compound, attribute):
                    data[compd_idx, attr_idx] = getattr(compound, attribute)
                else:
                    data[compd_idx, attr_idx] = np.nan

        hasz_morethan_50 = np.zeros(len(self.compounds))
        for compound_idx, compound in enumerate(self.compounds):
            if hasattr(compound, "symbols"):
                hasz_morethan_50[compound_idx] = list_has_element_with_atomic_number_greater_than_50(compound.symbols)
            else:
                hasz_morethan_50[compound_idx] = np.nan

        df = pd.DataFrame(data, columns=self.attributes, index=None)
        df["Has_Z>50"] = hasz_morethan_50.astype(bool)
        logging.info("Created dataframe of all attributes")
        df = df[self.attributes]

        return df
    

if __name__ == "__main__":
    database_path = "/Users/archismanchakraborti/Desktop/python_files/HRI_Research_Work/Data_management/artifacts/db_files/abse3.db"
    dataingestion = DataIngestion(database_path)
    compounds = dataingestion.convert_db_to_list()

    transformer = DataTransformation(compounds)
    df = transformer.create_df()
    print(df)


