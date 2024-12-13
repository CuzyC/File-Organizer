# PYTHON FILE ORGANIZER

import os
import shutil

# Path for the files to be organized
FILE_PATH = "test" #Change this path before running

# Create a directory if it does not already exist
def create_dir(dir_path):
    # print(dir)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

# Get the list of files in a directory
def check_file(dir):
    return os.listdir(dir)

# Extract and return the file extension in lowercase
def get_file_ext(file_path):
    return os.path.splitext(file_path)[1].lower()

# Organize files into folders based on their extensions
def organize_files(src_folder, dst_folder):
    files = check_file(src_folder)
    # print(files)

    for file in files:
        file_path = os.path.join(src_folder, file)

        if check_file:
            extension = get_file_ext(file).strip('.')
            # print(extension)

            if extension:
                directory = os.path.join(dst_folder, extension.upper()+'_Files')
                create_dir(directory)
                shutil.move(file_path, os.path.join(directory, file))

# Main function to organize files in the directory
def main(dir):

    create_dir(dir)
    organize_files(dir,dir)

    print('Files Organized Successfully')

if __name__ == "__main__":
    main(FILE_PATH)



