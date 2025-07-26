import h5py

file_path = r"C:\Users\91911\OneDrive\Desktop\Documents\Major_Project\exe_folder\model\model\final_model.h5"

try:
    with h5py.File(file_path, "r") as file:
        print("File opened successfully!")
        print("Contents:", list(file.keys()))  # List dataset names
except OSError:
    print("Error: The file is not a valid HDF5 file or is corrupted.")
