from pathlib import Path
if __name__ == '__main__':

    print([myvar for myvar in  Path("C:/Users/drakeredwind01").rglob("*") if "Microsoft Visual Studio/Shared/Python37_64/python" in file.read_text()]
