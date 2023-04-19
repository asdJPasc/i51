import os
import datetime

# Define function to rename files recursively
def rename_files(folder_path, day):
    # Get number of existing files in folder
    num_existing_files = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])

    # Get list of files sorted by modification time
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    files = sorted(files, key=lambda f: os.stat(os.path.join(folder_path, f)).st_mtime)

    # Loop through subfolders
    for subfolder in os.listdir(folder_path):
        # Check if subfolder is a folder
        if not os.path.isdir(os.path.join(folder_path, subfolder)):
            continue

        # Recursive call
        subfolder_path = os.path.join(folder_path, subfolder)
        rename_files(subfolder_path, day)

        # Get list of files sorted by modification time
        sub_files = [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))]
        sub_files = sorted(sub_files, key=lambda f: os.stat(os.path.join(subfolder_path, f)).st_mtime)

        # Loop through files in subfolder
        for i, filename in enumerate(sub_files):
            # Check if file is a Python script or a folder
            if os.path.isdir(os.path.join(subfolder_path, filename)): #or filename.endswith(".py") or filename.endswith(".txt"):
                continue

            # Separate file name and extension
            file_name, file_extension = os.path.splitext(filename)

            # Construct new file name with modified "month-day" part
            new_file_name = f"{day}{file_name[5:]}{file_extension}"

            # Rename file
            os.rename(os.path.join(subfolder_path, filename), os.path.join(subfolder_path, new_file_name))

# Prompt user for day of the file name
day = input("Enter the day (in MM-DD format) for the file name: ")

# Call function with current directory as argument
rename_files(os.getcwd(), day)
