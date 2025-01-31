# Choices
num = int(input("Enter a number: "))

print("Choices:")
print("a. @")
print("b. *")
print("c. 1")
operator = input("Choose operator: ")

# Conditions
if operator == "a":
    row = 1
    column = num
    while row <= column:
        print("@" * row)
        row += 1

elif operator == "b":
    row = 1
    column = num
    while row <= column:
        print("*" * row)
        row += 1

elif operator == "c":
    row = 1
    column = num
    while row <= column:
        num_in_row = 1
        while num_in_row <= row:
            print(num_in_row, end='')
            num_in_row += 1
        print("") 
        row += 1

else:
    print("Invalid input")
