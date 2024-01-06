import yaml

def add_units(config_file, num_batches):
  """
  Adds units for a specified number of batches based on a YAML configuration file.

  Args:
    config_file: Path to the YAML configuration file.
    num_batches: Number of batches.
  """
  # Load the YAML configuration
  with open(config_file, 'r') as f:
    config = yaml.safe_load(f)

  # Get the units
  units = config['units']

  # Calculate the total units
  total_units = sum(units.values()) * num_batches

  # Print the units
  for key, value in units.items():
    print(f"{key}: {value * num_batches} ({value}/{total_units} per batch)")

# Get the number of batches from the user
num_batches = int(input("Enter the number of batches: "))

# Get the YAML configuration file path from the user
config_file = input("Enter the path to the YAML configuration file: ")

# Add the units
add_units(config_file, num_batches)
