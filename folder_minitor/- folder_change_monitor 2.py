import os
import time
from tqdm import tqdm

def get_folders_and_sizes(root_dir):
    folders = []
    folder_sizes = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        total_folders = len(dirnames)
        with tqdm(total=total_folders, desc="Processing") as pbar:
            for folder in dirnames:
                folder_path = os.path.join(dirpath, folder)
                folder_size = os.path.getsize(folder_path)

                folders.append(folder)
                folder_sizes.append(folder_size)

                pbar.update(1)  # Update the progress bar for each folder

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
