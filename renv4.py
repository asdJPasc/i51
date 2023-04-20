import os
import datetime

def rename_files(folder_path, day):
    num_existing_files = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    files = sorted(files, key=lambda f: os.stat(os.path.join(folder_path, f)).st_mtime)

    for subfolder in os.listdir(folder_path):
        if not os.path.isdir(os.path.join(folder_path, subfolder)):
            continue

        subfolder_path = os.path.join(folder_path, subfolder)
        rename_files(subfolder_path, day)

        sub_files = [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))]
        sub_files = sorted(sub_files, key=lambda f: os.stat(os.path.join(subfolder_path, f)).st_mtime)

        for i, filename in enumerate(sub_files):
            if os.path.isdir(os.path.join(subfolder_path, filename)):
                continue

            file_name, file_extension = os.path.splitext(filename)

            new_file_name = f"{day}{file_name[5:]}{file_extension}"

            os.rename(os.path.join(subfolder_path, filename), os.path.join(subfolder_path, new_file_name))

day = input("Enter the day (in MM-DD format) for the file name: ")

rename_files(os.getcwd(), day)
