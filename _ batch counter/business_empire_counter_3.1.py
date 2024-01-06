import yaml

def calculate_buildings(config_file, available_money):
    """
    Calculates the maximum number of each building that can be constructed with the available money,
    along with the required units of each material.
    """

    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)

    costs = config['costs']
    buildings = config['private_house'], config['office_building'], config['trade_center'], config['skyscraper']

    building_plan = {}
    remaining_money = available_money
    total_cost = 0

    for building in sorted(buildings, key=lambda b: sum(costs[unit] * b['units'][unit] for unit in b['units']), reverse=True):
        building_cost = sum(costs[unit] * building['units'][unit] for unit in building['units'])
        max_buildings = int(remaining_money / building_cost)

        if max_buildings > 0:
            building_type = list(building['units'].keys())[0]
            building_plan[building_type] = {
                'number': max_buildings,
                'units': {unit: building['units'][unit] * max_buildings for unit in building['units']}
            }
            remaining_money -= building_cost * max_buildings
            total_cost += building_cost * max_buildings

    return building_plan, total_cost


# Get the path to the YAML configuration file
config_file = "D:/Documents/github/Free-time-coding/_ batch counter/business_empire_counter_yaml_config.yaml"

# Get the available money from the user
available_money = float(input("Enter the available amount of money: "))

# Call the function to create the building plan and total cost
building_plan, total_cost = calculate_buildings(config_file, available_money)

# Now you can use building_plan here
print("Building Plan:")
for building_type, building_data in building_plan.items():
    print(f"- {building_type}: {building_data['number']}")
    print(f"  Units: {building_data['units']}")
print(f"Total cost for {sum(building_data['number'] for building_data in building_plan.values())} buildings: ${total_cost:.2f}")
