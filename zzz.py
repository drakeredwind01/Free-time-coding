def process_transaction_line(line):
  """
  Processes a single line from the transaction history file, extracting relevant data.

  Args:
      line (str): A line from the transaction history file.

  Returns:
      dict: A dictionary containing parsed information from the line.
  """
  # Split the line based on commas, handling potential extra commas
  data = line.strip().split(",")
  information = {}

  # Extract data based on expected positions in the file format
  if len(data) >= 8:
    information["description"] = data[1].strip()  # Description (e.g., PAYPAL *LUMI...)
    information["date"] = data[3].strip()  # Date (e.g., 02/06/24)
    information["days_ago"] = data[4].strip()  # Days ago (e.g., yesterday)
    information["category"] = data[6].strip() if len(data) >= 7 else None  # Category (e.g., DiningOut)
    information["amount"] = data[7].strip()  # Amount (e.g., -$39.99)
    information["balance"] = data[8].strip()  # Balance (e.g., $785.10)
  else:
    print(f"Warning: Skipping line due to unexpected format: {line}")

  return information

if __name__ == '__main__':
  with open('Transaction_History.txt', 'r') as file:
    transactions = []
    for line in file:
      # Skip the header line
      if line.startswith('"'):
        continue
      transaction_data = process_transaction_line(line)
      if transaction_data:
        transactions.append(transaction_data)

  print("Transaction History:")
  for transaction in transactions:
    print(f"Description: {transaction['description']}")
    print(f"Date: {transaction['date']}")
    print(f"Days Ago: {transaction['days_ago']}")
    print(f"Category: {transaction['category']}")
    print(f"Amount: {transaction['amount']}")
    print(f"Balance: {transaction['balance']}")
    print("-" * 20)  # Separator between transactions
