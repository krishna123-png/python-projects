print('''Prices:
Bubblegum: $2
Toffee: $0.2
Ice cream: $5
Milk chocolate: $4
Doughnut: $2.5
Pancake: $3.2''')

items = ["Bubblegum", "Toffee", "Ice cream", "Milk chocolate", "Doughnut", "Pancake"]
earnings = [202, 118, 2250, 1680, 1075, 80]

income = 0
for index in range(len(earnings)):
    income = income + earnings[index]

print("Earned amount:")

for item in range(len(items)):
    print("{}: {}".format(items[item], earnings[item]))

print()
print("Income: {}".format(income))

staff_expense = int(input("Staff expenses:"))
other_expense = int(input("Other expenses:"))
print("Net income: $", income - staff_expense - other_expense)
