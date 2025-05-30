import os
import sys

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
      # Create the output file.
      with open(output_file_path, "wb") as output_file:
        # Read the XNB file.
        with open(file_path, "rb") as input_file:
          input_file_data = input_file.read()

        # Write the XNB file data to the output file.
        output_file.write(input_file_data)
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
