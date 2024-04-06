def process_transaction_line(line):
  """
  Processes a single line from the transaction history file, extracting relevant data.

  Args:
      line (str): A line from the transaction history file.

  Returns:
      dict (optional): A dictionary containing parsed information from the line,
                       or None if the line has unexpected format.
  """
  data = line.strip().split(",")
  information = {}

  if len(data) >= 8:
    # Access data elements using a try-except block for safer handling
    try:
      information["detail"] = data[1]
      information["date_and_days_ago"] = data[3]
      information["big_picture"] = data[5]
      information["money_change"] = data[7]
      # Access total money only if the list has at least 9 elements
      if len(data) >= 9:
        information["total_money"] = data[8]
    except IndexError:
      print(f"Warning: Skipping line due to unexpected format: {line}")
      return None  # Indicate line skipped

  else:
    print(f"Warning: Skipping line due to unexpected format: {line}")
    return None  # Indicate line skipped

  return information

with open('Transaction_History.txt', 'r') as file:
  Transaction_dict = {}
  for line in file:
    transaction_data = process_transaction_line(line)
    if transaction_data:
      Transaction_dict[transaction_data["detail"]] = transaction_data

print("Transaction History:")
for detail, transaction_info in Transaction_dict.items():
  # Check if 'total_money' key exists before accessing it
  if 'total_money' in transaction_info:
    print(f"Description: {detail}")
    print(f"Date and Days Ago: {transaction_info['date_and_days_ago']}")
    print(f"Big Picture: {transaction_info['big_picture']}")
    print(f"Money Change: {transaction_info['money_change']}")
    print(f"Total Money: {transaction_info['total_money']}")
  else:
    print(f"Description: {detail}")
    print(f"Data Incomplete (missing total money)")
  print("-" * 20)  # Separator between transactions
