expenses = [10.50, 8, 5, 15, 20, 5, 3]

soma = 0

for x in expenses:
    soma = soma + x

print("You spent $", soma, sep = '')

print("----------------------------")

expenses = [10.50, 8, 5, 15, 20, 5, 3]

total = sum(expenses)

print("You spent $", total, sep = '')