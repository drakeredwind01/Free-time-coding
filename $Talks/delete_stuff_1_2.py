import os

def delete_files(file_paths):
    for file_path in file_paths:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        else:
            print(f"File not found: {file_path}")

def delete_directory_contents(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
            print(f"Deleted: {file_path}")

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
    delete_directory_contents("C:\\Users\\drake\\AppData\\Local\\Temp\\")


'''
this is great but if a file is being used i get this error:



C:\Users\drake\.conda\envs\tf\python.exe D:\Documents\github\Free-time-coding\$Talks\delete_stuff_1_2.py 
Deleted: C:\Users\drake\AppData\Local\Temp\mat-debug-6436.log
Deleted: C:\Users\drake\AppData\Local\Temp\mat-debug-9724.log
Traceback (most recent call last):
  File "D:\Documents\github\Free-time-coding\$Talks\delete_stuff_1_2.py", line 30, in <module>
    delete_directory_contents("C:\\Users\\drake\\AppData\\Local\\Temp\\")
  File "D:\Documents\github\Free-time-coding\$Talks\delete_stuff_1_2.py", line 15, in delete_directory_contents
    os.remove(file_path)
PermissionError: [WinError 32] The process cannot access the file because it is being used by another process: 'C:\\Users\\drake\\AppData\\Local\\Temp\\051f21bb-ae23-45cc-85d2-846fb5ae4dea.tmp'

Process finished with exit code 1



try to make a script that uses try scripts to bypass such files and try to delete the rest of them



'''