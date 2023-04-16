import os
import datetime

# Define function to rename files recursively
def rename_files(folder_path, day):
    # Get number of existing files in folder
    num_existing_files = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])

    # Get list of files sorted by modification time
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    files = sorted(files, key=lambda f: os.stat(os.path.join(folder_path, f)).st_mtime)

    # Loop through files in folder
    for i, filename in enumerate(files):
        # Check if file is a Python script or a folder
        if os.path.isdir(os.path.join(folder_path, filename)) or filename.endswith(".py"):
            continue

        # Construct new file name
        file_extension = os.path.splitext(filename)[1]
        new_filename = f"{day}-3rd_i51-{i + 1}{file_extension}"

        # Rename file
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

    # Loop through subfolders
    for subfolder in os.listdir(folder_path):
        # Check if subfolder is a folder
        if not os.path.isdir(os.path.join(folder_path, subfolder)):
            continue

        # Recursive call
        subfolder_path = os.path.join(folder_path, subfolder)
        rename_files(subfolder_path, day)

# Prompt user for day of the file name
day = input("Enter the day (in MM-DD format) for the file name: ")

# Call function with current directory as argument
rename_files(os.getcwd(), day)
