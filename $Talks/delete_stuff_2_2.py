import os

def delete_files(file_paths):
    for file_path in file_paths:
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            else:
                print(f"File not found: {file_path}")
        except OSError as e:
            print(f"Error deleting {file_path}: {e}")

def delete_directory_contents(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except OSError as e:
                print(f"Error deleting {file_path}: {e}")

# Specific files to delete
files_to_delete = [
    "C:\\Users\\drake\\AppData\\Local\\Temp\\mat-debug-6436.log",
    "C:\\Users\\drake\\AppData\\Local\\Temp\\mat-debug-9724.log",
    # ... other files ...
]

if __name__ == "__main__":
    # Delete specific files
    delete_files(files_to_delete)

    # Delete all files in the Temp directory
    delete_directory_contents("C:/Users/drake/AppData/Local/Temp/")


'''
pretty good, but i think it would be better if it out putted some data (date - ah)
make it out put the size of the files and how many of them there were and are.
put the size difference under the amounts and have an arrow pointing to the two instances of differences
'''