import os
import time
import csv

folder_path = r'C:\Windows\SoftwareDistribution\Download'


if __name__ == '__main__':

    def delete_folder_contents():
        folder_size = 0
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path):
                    folder_size += os.path.getsize(file_path)
                    os.unlink(file_path)
            except Exception as e:
                print(e)
        return folder_size

    while True:
        if os.path.isdir(folder_path):
            if os.listdir(folder_path) != []:
                folder_size = delete_folder_contents()
                with open('data_restored.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([time.strftime('%Y-%m-%d %H:%M:%S'), folder_size])
        time.sleep(60)
