import yaml

def calculate_skyscrapers_and_costs(config_file, gross_total):
   """
   Calculates the number of skyscrapers that can be built and the required units and costs,
   given a gross total budget and a YAML configuration file.

   Args:
       config_file: Path to the YAML configuration file.
       gross_total: The gross total budget available.
   """

   # Load the YAML configuration
   with open(config_file, 'r') as f:
       config = yaml.safe_load(f)

   # Get units and costs
   units = config['units']
   costs = config['costs']

   # Calculate the cost per skyscraper
   cost_per_skyscraper = sum(units[key] * costs[key] for key in units.keys())

   # Determine the maximum number of skyscrapers that can be built
   max_skyscrapers = gross_total // cost_per_skyscraper

   # Calculate the total units and cost for the maximum number of skyscrapers
   total_units = {key: value * max_skyscrapers for key, value in units.items()}
   total_cost = cost_per_skyscraper * max_skyscrapers

   # Print the results
   print(f"Maximum number of skyscrapers that can be built: {max_skyscrapers}")

   for key, value in total_units.items():
       unit_cost = costs[key] * value
       print(f"{key}: {value} units, costing ${unit_cost:.2f} total")

   print(f"Total expected cost: ${total_cost:.2f}")

# Get the gross total from the user
gross_total = float(input("Enter the gross total budget: "))

# Get the YAML configuration file path from the user
# config_file = input("Enter the path to the YAML configuration file: ")  # Prompt for input
config_file = "D:/Documents/github/Free-time-coding/_ batch counter/batch_counter_yaml_skyscraper_config.yaml"  # Or use a hardcoded path

# Calculate skyscrapers and costs
calculate_skyscrapers_and_costs(config_file, gross_total)
