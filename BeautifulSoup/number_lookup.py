


with open('name_number.txt', 'r') as file:
  name_number_dict = {}
  for line in file:
    name, number = line.strip().split()  # Split line into name and number
    name_number_dict[name] = number  # Add name-number pair to dictionary

print("Names and Numbers:")
for name, number in name_number_dict.items():
  print(f"{name}: {number}")  # Print name and number in a formatted way

while True:
  query = input("Please enter your query: ")
  if query == 'quit':
    break
  if query in name_number_dict:
    print(name_number_dict[query])
  else:
    print('not found')












