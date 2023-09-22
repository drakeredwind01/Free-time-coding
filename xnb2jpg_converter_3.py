'''

2023.09.22.10.16.50.514
	C:\Users\drakeredwind01>python "D:\documents\GitHub\Free time coding\xnb2jpg_converter_2.py" "D:\Program Files (x86)\Steam\steamapps\common\Terraria\Content\Images\Accessories" "D:\documents\temp\terrria items"
	Error converting XNB file 'D:\Program Files (x86)\Steam\steamapps\common\Terraria\Content\Images\Accessories\Acc_HandsOff_1.xnb' to JPG file 'D:\documents\temp\terrria items\Acc_HandsOff_1.jpg': 'utf-8' codec can't decode byte 0x80 in position 5: invalid start byte
	Error converting XNB file 'D:\Program Files (x86)\Steam\steamapps\common\Terraria\Content\Images\Accessories\Acc_HandsOff_10.xnb' to JPG file 'D:\documents\temp\terrria items\Acc_HandsOff_10.jpg': 'utf-8' codec can't decode byte 0x80 in position 5: invalid start byte
	file is not encoding in UTF-8
2023.09.22.10.21.27.760
    C:\Users\drakeredwind01>python "D:\documents\GitHub\Free time coding\xnb2jpg_converter_3.py" "D:\Program Files (x86)\Steam\steamapps\common\Terraria\Content\Images\Accessories" "D:\documents\temp\terrria items"
    Error converting XNB file 'D:\Program Files (x86)\Steam\steamapps\common\Terraria\Content\Images\Accessories\Acc_HandsOff_1.xnb' to JPG file 'D:\documents\temp\terrria items\Acc_HandsOff_1.jpg': 'ascii' codec can't decode byte 0x80 in position 5: ordinal not in range(128)
    Error converting XNB file 'D:\Program Files (x86)\Steam\steamapps\common\Terraria\Content\Images\Accessories\Acc_HandsOff_10.xnb' to JPG file 'D:\documents\temp\terrria items\Acc_HandsOff_10.jpg': 'ascii' codec can't decode byte 0x80 in position 5: ordinal not in range(128)
    Error converting XNB file 'D:\Program Files (x86)\Steam\steamapps\common\Terraria\Content\Images\Accessories\Acc_HandsOff_11.xnb' to JPG file 'D:\documents\temp\terrria items\Acc_HandsOff_11.jpg': 'ascii' codec can't decode byte 0x80 in position 5: ordinal not in range(128)
    'ascii' codec can't decode byte 0x80 in position 5: ordinal not in range(128) means that the XNB file contains a byte that cannot be decoded using the ASCII encoding.
      I'm done
      tried opening the original files and they don't open either so nothing I do will work







'''



import os
import sys
import pathlib
from PIL import Image

def convert_xnb_to_jpg(from_folder, to_folder):
  """Converts all XNB files in the given folder to JPG files and saves them to the given output folder.

  Args:
    from_folder: The path to the folder containing the XNB files to convert.
    to_folder: The path to the folder to save the converted JPG files to.
  """

  # Create the output folder if it doesn't exist.
  if not os.path.exists(to_folder):
    os.makedirs(to_folder)

  # Iterate over all files in the input folder.
  for file in os.listdir(from_folder):
    # Get the full path to the file.
    file_path = os.path.join(from_folder, file)

    # Skip files that are not XNB files.
    if not file.endswith(".xnb"):
      continue

    # Create the output file path.
    output_file_path = os.path.join(to_folder, file.replace(".xnb", ".jpg"))

    # Try to convert the XNB file to a JPG file.
    try:
      # Open the XNB file using the ASCII encoding.
      with pathlib.Path(file_path).read_text(encoding="ASCII") as input_file:
        # Read the XNB file data.
        input_file_data = input_file.read()

      # Decode the XNB file data into an Image object.
      image = Image.open(input_file_data)

      # Save the Image object as a JPG file.
      image.save(output_file_path, "JPEG")
    except Exception as e:
      # Print an error message if the conversion fails.
      print(f"Error converting XNB file '{file_path}' to JPG file '{output_file_path}': {e}")

def main(from_folder, to_folder):
  """Converts all XNB files in the given folder to JPG files and saves them to the given output folder.

  Args:
    from_folder: The path to the folder containing the XNB files to convert.
    to_folder: The path to the folder to save the converted JPG files to.
  """

  # Check if the from folder exists.
  if not os.path.exists(from_folder):
    print(f"Error: From folder '{from_folder}' does not exist.")
    sys.exit(1)

  # Check if the to folder exists.
  if not os.path.exists(to_folder):
    print(f"Error: To folder '{to_folder}' does not exist.")
    sys.exit(1)

  # Convert all XNB files in the from folder to JPG files and save them to the to folder.
  convert_xnb_to_jpg(from_folder, to_folder)

if __name__ == "__main__":
  # Get the from and to folders from the command line arguments.
  from_folder = sys.argv[1] if len(sys.argv) > 1 else "."
  to_folder = sys.argv[2] if len(sys.argv) > 2 else "converted_jpgs"

  # Convert all XNB files in the from folder to JPG files and save them to the to folder.
  main(from_folder, to_folder)
