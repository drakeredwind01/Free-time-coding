

'''
locale module is used to format the folder_size variable with commas every three digits.
The n format specifier achieves this.

2023.04.04.23.16.05.286
new variable scan_interval which is the number of seconds to wait in between scans.
The program will print out "Deletion finished. Checking again..."
after it has deleted all the files and folders in the directory,
and then it will wait for scan_interval seconds before checking again.
If the folder is empty, it will print out "Folder is empty."
If the folder path is invalid, it will print out "Folder path is invalid."


'''


import os
import time
import csv
import shutil
import locale

folder_path = r'C:\Windows\SoftwareDistribution\Download'
scan_interval = 60 # seconds

# Set locale for comma separator in folder size
locale.setlocale(locale.LC_ALL, '')

if __name__ == '__main__':

    def delete_folder_contents():
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

                # Delete file
                os.remove(file_path)

                # Update counts
                file_count += 1
                folder_size += file_size

            for dir in dirs:
                # Get folder path
                folder_path = os.path.join(root, dir)

                # Delete folder
                shutil.rmtree(folder_path)

                # Update counts
                folder_count += 1

        # Return counts
        return file_count, folder_count, folder_size


    while True:
        if os.path.isdir(folder_path):
            if os.listdir(folder_path) != []:
                print("Folder is not empty! Analyzing...")
                file_count, folder_count, folder_size = delete_folder_contents()
                print(f"{folder_size:n} bytes of data, {folder_count} folders, and {file_count} files were deleted.")
                with open('data_restored.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([time.strftime('%Y-%m-%d %H:%M:%S'), folder_size])
                print("Deletion finished. Checking again...")
            else:
                print("Folder is empty.")
        else:
            print("Folder path is invalid.")

        time.sleep(scan_interval)
