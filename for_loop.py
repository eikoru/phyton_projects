# Inputs and operations
fnum = int(input("Enter number of Inputs: "))
print("Choose Operators:")
print(" 1. Addition")
print(" 2. Multiplication")

operator = input("Enter Operator: ")

# Looping
if operator == '1':
    total_sum = 0
    for row in range(fnum):
        total_sum += int(input("Please input the #" + str(row + 1) + " number: "))
    print("The total sum is:", total_sum)

elif operator == '2':
    total_product = 1
    for row in range(fnum):
        total_product *= int(input("Please input the #" + str(row + 1) + " number: "))
    print("The total product is:", total_product)

else:
    print("Invalid Operator")
