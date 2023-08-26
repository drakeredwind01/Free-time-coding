

'''

- folder_change_monitor 2.py
  ouput:
    Processing: 100%|██████████| 31/31 [00:00<00:00, 11998.10it/s]
    Processing: 100%|██████████| 5/5 [00:00<?, ?it/s]
    Processing: 0it [00:00, ?it/s]
    Processing: 100%|██████████| 1/1 [00:00<?, ?it/s]
    Processing: 100%|██████████| 1/1 [00:00<?, ?it/s]
    Processing: 0it [00:00, ?it/s]
    Processing: 0it [00:00, ?it/s]
  trying to have it look at the total folders before making the progress bar
- folder_change_monitor 3.py
  want the program to count the number of folders while it is running
- folder_change_monitor 4.py
  I think it's working but I think it's tryingto print it too fast
  so now it's not readable



'''


import os
import time

def get_folders_and_sizes(root_dir):
  folders = []
  folder_sizes = []

  for dirpath, dirnames, filenames in os.walk(root_dir):
    for folder in dirnames:
      folder_path = os.path.join(dirpath, folder)
      folder_size = os.path.getsize(folder_path)

      folders.append(folder)
      folder_sizes.append(folder_size)

  return folders, folder_sizes

def main():
  # Get the current time.
  current_time = time.time()

  # Get the list of all folders and their sizes on C:.
  root_dir = "C:\\"
  folders, folder_sizes = get_folders_and_sizes(root_dir)

  # Write the list of folders and their sizes to a CSV file.
  output_file_name = str(current_time) + "_folders_and_sizes" + ".csv"

  with open(output_file_name, "w") as output_file:
    writer = csv.writer(output_file)
    writer.writerows([(folder, folder_size) for folder, folder_size in zip(folders, folder_sizes)])

if __name__ == "__main__":
  main()
