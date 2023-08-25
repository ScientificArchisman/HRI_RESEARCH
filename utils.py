from ase import io
import os

def get_pocar_file(cif_files_path:str, output_directory:str, verbosity:int = 0) -> None:
    """Converts CIF file to POSCAR file
    Args:
        cif_file (str / list): File containing all cif files or a list of cif files
        output_directory (str): Output directory to store the POSCAR files
        verbosity (int): Verbosity level. 0 = No output, 1 = Print output. Defaults to 0.
    Returns:
        None
    """
    # Check if output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Check if cif_files is a string or a list
    if isinstance(cif_files_path, str):
        # Store filenames as a list 
        if verbosity == 1:
            print(f"Reading cif files from {cif_files_path}")
        cif_files = os.listdir(cif_files_path)
        cif_files = [os.path.join(cif_files_path, f) for f in cif_files if f.endswith(".cif")]

    elif isinstance(cif_files_path, list):
        cif_files = cif_files_path

    # Loop over all the cif files
    for cif_file in cif_files:
        atom = io.read(cif_file) # Read the cif file

        # Prepare the filepath for saving the poscar file
        output_file = os.path.join(output_directory, 
                                    cif_file.split("/")[-1].split(".")[0] + # Gets the filename without the extension
                                    ".poscar")
        if verbosity == 1:
            print(f"Writing POSCAR file to {output_file}")
        io.write(output_file, atom, format="vasp") # Write the POSCAR file


if __name__ == "__main__":
    output_directory = "/Users/archismanchakraborti/Desktop/python_files/HRI_Research_Work/Energy_optimization/Poscar_files"
    cif_files = "/Users/archismanchakraborti/Desktop/python_files/HRI_Research_Work/Energy_optimization/Pb7S2Br10"
    get_pocar_file(cif_files, output_directory)