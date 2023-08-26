

'''
This updated version of the code uses recursion to delete 
all files and folders within the specified folder path. 
If it encounters a folder, it calls itself with the folder 
path as an argument to delete the contents of the folder, 
and then it removes the empty folder using os.rmdir(). 
'''

import os
import time
import csv

folder_path = r'C:\Windows\SoftwareDistribution\Download'


if __name__ == '__main__':

    def delete_folder_contents():
        num_files_deleted = 0
        num_folders_deleted = 0
        total_bytes_deleted = 0
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for filename in files:
                file_path = os.path.join(root, filename)
                try:
                    if os.path.isfile(file_path):
                        total_bytes_deleted += os.path.getsize(file_path)
                        os.unlink(file_path)
                        num_files_deleted += 1
                except Exception as e:
                    print(e)
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                try:
                    if os.path.isdir(dir_path):
                        os.rmdir(dir_path)
                        num_folders_deleted += 1
                except Exception as e:
                    print(e)
        return num_files_deleted, num_folders_deleted, total_bytes_deleted

    while True:
        if os.path.isdir(folder_path):
            if os.listdir(folder_path) != []:
                print("Folder is not empty! Analyzing...")
                num_files_deleted, num_folders_deleted, total_bytes_deleted = delete_folder_contents()
                print(f"{num_files_deleted} files and {num_folders_deleted} folders were deleted, freeing up {total_bytes_deleted} bytes of disk space.")
                with open('data_restored.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([time.strftime('%Y-%m-%d %H:%M:%S'), total_bytes_deleted])
        time.sleep(60)
