#Choices
print("Choices: ")
print("1.Calculator ")

#choices_a,b,c,d
print("a.Addition")
print("b.Subtraction")
print("c.Multiplication")
print("d.Division")

#choices2
print("2.Positive or Negative number")

#choices3
print("3.Lowest Number")

#Input
choice=(input("Enter your choice:"))

#choices_1
if choice == '1':
    a="Addition"
    b="Subtraction"
    c="Multiplication"
    d="Division"
    fnum = int(input("Enter first number:"))
    snum = int(input("Enter second number:"))
    operator=(input("Enter arithmetic operator:"))

    if operator == 'a':
        sum=fnum+snum
        print("The sum of",fnum,"and",snum,"is",sum)
    elif operator == 'b':
        difference=fnum-snum
        print("The difference of",fnum,"and",snum,"is",difference)
    elif operator == 'c': 
        product=fnum*snum
        print("The product of", fnum,"and", snum,"is", product)
    elif operator == 'd':
        quotient = fnum / snum
        print("The quotient of", fnum, "and",snum,"is",quotient)

#choices_2
if choice == "2":
    num2=int(input("Enter number:"))
    if num2 > 0:
        print(num2,"is a positive number")
    elif num2 < 0:
        print(num2,"is a negative number")
    else:
        print(num2,"is a neutral number")

#choices_3
if choice == "3":
    fnum2=int(input("Enter first number:"))
    snum2=int(input("Enter second number:"))

    if fnum2 > snum2:
        print(fnum2,"is lower than", snum2)
    elif fnum2 < snum2:
        print(snum2,"is lower than", fnum2)

    elif fnum2 == snum2:
     print(fnum2,"is equal to", snum2)