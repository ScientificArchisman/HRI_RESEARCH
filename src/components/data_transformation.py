from src.logger import logging
import pandas as pd
from src.utils import load_pickle, list_has_element_with_atomic_number_greater_than_50
import os
import numpy as np


class DataTransformation:
    def __init__(self, compounds_database_path) -> None:
        self.root_data_path = os.path.join("artifacts", "data")
        self.attributes = ['formula', 'spacegroup', "Has_Z>50", 'thermodynamic_stability_level', 'workfunction',
                            'symbols',  'pbc', 'E_x', 'E_y', 'E_z', '_constrained_forces', '_constraints', '_data',
                            '_keys', 'asr_id', 'calculator', 'calculator_parameters', 'cell',
                            'cell_area', 'charge', 'cod_id', 'constrained_forces', 'constraints',
                            'crystal_type', 'ctime', 'dE_zx', 'dE_zy', 'data', 'dipole', 'dipz',
                            'dos_at_ef_nosoc', 'dos_at_ef_soc', 'efermi', 'ehull', 'energy', 'evac',
                            'evacdiff', 'first_class_material', 'fmax', 'folder', 'forces',
                            'gap', 'gap_dir', 'gap_dir_nosoc', 'gap_nosoc',
                            'has_asr_bader', 'has_asr_bandstructure',
                            'has_asr_bandstructure_calculate', 'has_asr_convex_hull',
                            'has_asr_database_material_fingerprint', 'has_asr_gs',
                            'has_asr_gs_calculate', 'has_asr_magnetic_anisotropy',
                            'has_asr_magstate', 'has_asr_pdos', 'has_asr_pdos_calculate',
                            'has_asr_projected_bandstructure', 'has_asr_relax', 'has_asr_setinfo',
                            'has_asr_setup_reduce', 'has_asr_structureinfo',
                            'has_inversion_symmetry', 'hform', 'id', 'initial_magmoms',
                            'is_magnetic', 'key_value_pairs', 'magmom', 'magmoms', 'magstate',
                            'mass', 'mtime', 'natoms', 'nspins', 'numbers', 'pointgroup',
                            'positions', 'smax', 'spgnum', 'spin_axis',
                            'stoichiometry', 'stress',
                            'uid', 'unique_id', 'user', 'volume']
        try:
            self.compounds = load_pickle(compounds_database_path)
        except Exception as e:
            logging.error("Failed to load pickle", e)
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

        df = pd.DataFrame(data, columns=self.attributes)
        df["Has_Z>50"] = hasz_morethan_50.astype(bool)
        logging.info("Created dataframe of all attributes")
        df = df[self.attributes]

        logging.info("Saving data to csv file")
        try:
            df.to_csv(os.path.join(self.root_data_path, "data.csv"))
        except Exception as e:
            logging.error("Error saving file to csv format", e)
            raise e
        logging.info("Saved dataframe to csv")
        return df
    

if __name__ == "__main__":
    compd_database_path = "artifacts/data/raw_data.pkl"
    transformer = DataTransformation(compd_database_path)
    df = transformer.create_df()