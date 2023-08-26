from pathlib import Path
home_directory = Path("C:/Users/drakeredwind01")
if __name__ == '__main__':

    print("starting")
    for file in home_directory.rglob("*"):
        try:
            if "Microsoft Visual Studio/Shared/Python37_64/python" in file.read_text():
                print(file.name)
        except:
            pass