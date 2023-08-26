

'''
delete temp data in folders

locale module is used to format the folder_size variable with commas every three digits.
The n format specifier achieves this.

2023.04.04.23.16.05.286
new variable scan_interval which is the number of seconds to wait in between scans.
The program will print out "Deletion finished. Checking again..."
after it has deleted all the files and folders in the directory,
and then it will wait for scan_interval seconds before checking again.
If the folder is empty, it will print out "Folder is empty."
If the folder path is invalid, it will print out "Folder path is invalid."

2023.04.05.00.08.39.130
the delete_folder_contents() function now takes a folder_path parameter,
which is passed from the main loop as it iterates through the list of folder paths.
Also, the folder path is included in the output when writing to the CSV file.


'''


import os
import time
import csv
import shutil
import locale

folder_paths = [r'C:\Windows\SoftwareDistribution\Download',
                r'C:\Users\drakeredwind01\AppData\Local\Microsoft\Windows\WebCache',
                r'%temp%',
                r'C:\Users\drakeredwind01\AppData\Local\Microsoft\Windows\INetCache',
                r'C:\Users\drakeredwind01\AppData\Local\Opera Software\Opera GX Stable\Cache\Cache_Data']

scan_interval = 320 # seconds

# Set locale for comma separator in folder size
locale.setlocale(locale.LC_ALL, '')

if __name__ == '__main__':

    def delete_folder_contents(folder_path):
        # Initialize counts
        file_count = 0
        folder_count = 0
        folder_size = 0

        # Walk through folder and subfolders
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Get file path and size
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)

                try:
                    # Delete file
                    os.remove(file_path)

                    # Update counts
                    file_count += 1
                    folder_size += file_size
                except:
                    print(f"Could not delete file: {file_path}")

            for dir in dirs:
                # Get folder path
                folder_path = os.path.join(root, dir)

                try:
                    # Delete folder
                    shutil.rmtree(folder_path)

                    # Update counts
                    folder_count += 1
                except:
                    print(f"Could not delete folder: {folder_path}")

        # Return counts
        return file_count, folder_count, folder_size


    while True:
        for folder_path in folder_paths:
            if os.path.isdir(folder_path):
                if os.listdir(folder_path) != []:
                    print(f"{folder_path}: Folder is not empty! Analyzing...")
                    file_count, folder_count, folder_size = delete_folder_contents(folder_path)
                    print(f"{folder_size:n} bytes of data, {folder_count} folders, and {file_count} files were deleted in {folder_path}.")
                    with open('data_restored.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([time.strftime('%Y-%m-%d %H:%M:%S'), folder_size, folder_path])
                    print(f"{folder_path}: Deletion finished. Checking again...")
                else:
                    print(f"{folder_path}: Folder is empty.")
            else:
                print(f"{folder_path}: Folder path is invalid.")

        time.sleep(scan_interval)
