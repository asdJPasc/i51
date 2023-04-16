import os

dir_path = os.getcwd()

files_to_delete = []

for root, dirs, files in os.walk(dir_path):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        # Check if current directory is not the same as the root directory
        if root != dir_path:
            files_to_delete.append(file_path)

if len(files_to_delete) == 0:
    print("No files found to delete.")
else:
    print(f"{len(files_to_delete)} files found to delete:\n")
    for file_path in files_to_delete:
        print(file_path)
    print()
    while True:
        confirm = input(f"Do you want to delete {len(files_to_delete)} files? (Y/N) ").strip().lower()
        if confirm == 'y':
            for file_path in files_to_delete:
                os.remove(file_path)
                print(f"{file_path} has been deleted.")
            break
        elif confirm == 'n':
            print("No files have been deleted.")
            break
        else:
            print("Invalid input. Please enter Y or N.")
