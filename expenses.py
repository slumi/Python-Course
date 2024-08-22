expenses = [10.50, 8, 5, 15, 20, 5, 3]

soma = 0

for x in expenses:
    soma = soma + x

print("You spent $", soma, sep = '')

print("----------------------------")

expenses = [10.50, 8, 5, 15, 20, 5, 3]

total = sum(expenses)

print("You spent $", total, sep = '')

print("-----------------------------")

total2 = 0
expenses2 = []
num_expenses = int(input("Enter # of expenses:"))

for i in range(num_expenses):
    expenses2.append(float(input("Enter an expense:")))

total2 = sum(expenses2)

print("You spent $", total2, sep='')
