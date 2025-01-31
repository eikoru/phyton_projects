#Choices
num=int(input("Enter a number:"))
print("Choices:")
print("a.@")
print("b.*")
print("c.1")

operator=(input("Choose operator:"))
#Conditions
if operator == "a":
    row = 1
    column = (num)
    while row < column:
        print("@" * row)
    row += 1

elif operator == "b":
    row = 1
    column = (num)
    while row < column:
        print("*" * row)
    row += 1

elif operator == "c":
    row = 1
    column = (num)
    while row < column:
        num = 1
    while num <= row:
     print(num,end = '' )
     num += 1
    print(" ")
    row += 1

else:
    print("Invalid input")
