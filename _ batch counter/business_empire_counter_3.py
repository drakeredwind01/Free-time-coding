  import yaml

  def calculate_buildings(config_file, available_money):
      """
      Calculates the maximum number of each building that can be constructed with the available money,
      along with the required units of each material.

      Args:
          config_file (str): Path to the YAML configuration file.
          available_money (float): The total amount of money available.

      Returns:
          dict: A dictionary containing the building types, number of buildings, and required units of each material.
      """

      with open(config_file, 'r') as f:
          config = yaml.safe_load(f)

      costs = config['costs']
      buildings = config['private_house'], config['office_building'], config['trade_center'], config['skyscraper']

      building_plan = {}
      remaining_money = available_money

      for building in sorted(buildings, key=lambda b: sum(costs[unit] * b['units'][unit] for unit in b['units']), reverse=True):
          # ... (other calculations)

          if max_buildings > 0:
              # Access the first key directly using list(building['units'].keys())[0]
              building_plan[list(building['units'].keys())[0]] = {
                  'number': max_buildings,
                  'units': {unit: building['units'][unit] * max_buildings for unit in building['units']}
              }
              remaining_money -= building_cost * max_buildings

      return building_plan

  # Get the path to the YAML configuration file
  config_file = "D:\Documents\github\Free-time-coding\_ batch counter\business_empire_counter_yaml_config.yaml"

  # Get the available money from the user
  available_money = float(input("Enter the available amount of money: "))

  # Calculate the building plan
  building_plan = calculate_buildings(config_file, available_money)

  # Print the building plan
  print("Building Plan:")
  for building_type, building_data in building_plan.items():
      print(f"- {building_type}: {building_data['number']}")
      print(f"  Units: {building_data['units']}")
