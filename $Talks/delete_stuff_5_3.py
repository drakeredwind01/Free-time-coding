import os
import datetime
from tqdm import tqdm

'''
added tqdm # i love this
'''
def delete_files(file_paths):
    total_size_before = 0
    total_files_before = len(file_paths)
    deleted_files = 0
    deleted_size = 0

    for file_path in file_paths:
        try:
            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                total_size_before += file_size
                os.remove(file_path)
                deleted_files += 1
                deleted_size += file_size
                print(f"Deleted: {file_path} ({file_size} bytes)")
            else:
                print(f"File not found: {file_path}")
        except OSError as e:
            print(f"Error deleting {file_path}: {e}")

    total_size_after = total_size_before - deleted_size
    total_files_after = total_files_before - deleted_files

    print(f"\nTotal files before deletion: {total_files_before}")
    print(f"Total size before deletion: {total_size_before} bytes")
    print(f"Total files after deletion: {total_files_after}")
    print(f"Total size after deletion: {total_size_after} bytes")

    print(f"\nSize difference: {deleted_size} bytes")
    print(f"File count difference: {deleted_files}")

    print(f"\nFiles: {total_files_before} - {deleted_files} = {total_files_after}")
    print(f"Size: {total_size_before} bytes - {deleted_size} bytes = {total_size_after} bytes")


def delete_directory_contents(directory_path):
    total_size_before = 0
    total_files_before = 0
    deleted_files = 0
    deleted_size = 0

    for root, dirs, files in os.walk(directory_path):
        # for file in tqdm(files, desc=f"Deleting files in {root}", unit="file"):
        for file in tqdm(files, desc=f"Deleting files ", unit="file"):
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)
                total_size_before += file_size
                total_files_before += 1
                os.remove(file_path)
                deleted_files += 1
                deleted_size += file_size
                # print(f"Deleted: {file_path} ({file_size} bytes)")  # Removed for cleaner output
            # except OSError as e:
            except:
                pass
                # print(f"Error deleting {file_path}: {e}")

    total_size_after = total_size_before - deleted_size
    total_files_after = total_files_before - deleted_files

    print(f"\nTotal files before deletion: {total_files_before}")
    print(f"Total size before deletion: {total_size_before} bytes")
    print(f"Total files after deletion: {total_files_after}")
    print(f"Total size after deletion: {total_size_after} bytes")

    print(f"\nSize difference: {deleted_size} bytes")
    print(f"File count difference: {deleted_files}")

    print(f"\nFiles: {total_files_before} - {deleted_files} = {total_files_after}")
    print(f"Size: {total_size_before} bytes - {deleted_size} bytes = {total_size_after} bytes")

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
    delete_directory_contents("C:/Windows/SoftwareDistribution/Download/")
