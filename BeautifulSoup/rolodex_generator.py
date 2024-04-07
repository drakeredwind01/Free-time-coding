import random

first_names = ["John", "Jane", "David", "Lisa", "Michael", "Jessica", "James", "Ashley", "Robert", "Sarah",
               "Matthew", "Emily", "William", "Jennifer", "Joseph", "Stephanie", "Andrew", "Amanda", "Daniel",
               "Nicole", "Benjamin", "Samantha", "Charles", "Brittany", "Richard", "Vanessa", "Kevin", "Catherine",
               "Joseph", "Elizabeth", "Thomas", "Lauren", "Christopher", "Alexis", "Jacob", "Kayla", "Ryan", "Megan",
               "Joshua", "Victoria", "Nicholas", "Olivia", "Daniel", "Sophia", "Ethan", "Isabella", "Andrew",
               "Charlotte",
               "Matthew", "Mia", "David", "Abigail", "Joseph", "Evelyn", "William", "Avery", "Brandon", "Emily"]

last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez",
              "Wilson", "Moore", "Lewis", "Lee", "Walker", "Allen", "Young", "Hall", "Hernandez", "King",
              "Nelson", "Clark", "Wright", "Lopez", "Martin", "Anderson", "Scott", "Thomas", "Hernandez",
              "Garcia", "Rodriguez", "Baker", "Harris", "Sanchez", "Ramirez", "Robinson", "Moore", "Lewis",
              "Walker", "Allen", "YoungKing", "Wright", "Lopez", "Martin", "Anderson", "Scott", "Thomas",
              "Hernandez", "Garcia", "Rodriguez"]

phone_numbers = []
for _ in range(100):
  # Generate random 3-digit area code
  area_code = f"{random.randint(100, 999)}-"

  # Generate random 3-digit prefix and 4-digit line number
  prefix = f"{random.randint(100, 999)}-"
  line_number = f"{random.randint(1000, 9999)}"

  # Combine area code, prefix, and line number
  phone_numbers.append(f"{area_code}{prefix}{line_number}")

# Ensure rolodex and phone_numbers have the same length
rolodex = []
for i in range(len(phone_numbers)):  # Use the length of phone_numbers
  first_name = random.choice(first_names)
  last_name = random.choice(last_names)
  full_name = f"{first_name} {last_name}"
  phone_number = phone_numbers[i]
  rolodex.append(f"{full_name} - {phone_number}")

# Write rolodex to a file
with open('rolodex.txt', 'w') as file:
  for entry in rolodex:
    file.write(f"{entry}\n")  # Write each entry with a newline character

# Print confirmation message (optional)
print("Rolodex written to 'rolodex.txt'")
