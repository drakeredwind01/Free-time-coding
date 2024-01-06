import yaml

def add_units_and_cost(config_file, num_batches):
  """
  Adds units and calculates total cost for a specified number of batches based on a YAML configuration file.

  Args:
    config_file: Path to the YAML configuration file.
    num_batches: Number of batches.
  """
  # Load the YAML configuration
  with open(config_file, 'r') as f:
    config = yaml.safe_load(f)

  # Get units and costs
  units = config['units']
  costs = config['costs']

  # Calculate total units and cost per batch
  total_units = sum(units.values()) * num_batches
  total_cost_per_batch = sum([costs[key] * units[key] for key in units.keys()])

  # Calculate total cost
  total_cost = total_cost_per_batch * num_batches

  # Print units and costs
  for key, value in units.items():
    unit_cost = costs[key] * value
    print(f"{key}: {value * num_batches} units ({value}/{total_units} per batch), costing ${unit_cost:.2f} per batch and ${unit_cost * num_batches:.2f} total")

  print(f"Total cost for {num_batches} batches: ${total_cost:.2f}")

# Get the number of batches from the user
num_batches = int(input("Enter the number of batches: "))

# Get the YAML configuration file path from the user
# config_file = input("Enter the path to the YAML configuration file: ")
# config_file = "D:/Documents/github/Free-time-coding/_ batch counter/batch_counter_yaml_2_config.yaml"
config_file = "D:/Documents/github/Free-time-coding/_ batch counter/batch_counter_yaml_skyscraper_config.yaml"

# Add units and calculate cost
add_units_and_cost(config_file, num_batches)
