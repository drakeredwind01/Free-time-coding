import re
with open('Transaction_History.txt', 'r') as file:
  Transaction_dict = {}
  next(file)  # Skip the header line
  for line in file:
    # empty1, detail, date_and_days_ago, empty2, big_picture, empty3, money_change, total_money = line.strip().split(",")   # get 2
    empty1, detail, date_and_days_ago, empty2, big_picture, empty3, money_change, total_money = re.findall(r'(.+?)(?:, | $)', line.strip())   # get 0
    Transaction_dict[detail] = [empty1, date_and_days_ago, empty2, big_picture, empty3, money_change, total_money]

print("Names and Numbers:")
for empty1,detail,date_and_days_ago,empty2,big_picture,empty3,money_change,total_money in Transaction_dict.items():
  print(f"{empty1}: {detail}: {date_and_days_ago}: {empty2}: {big_picture}: {empty3}: {money_change}: {total_money}")  # Print name and number in a formatted way












