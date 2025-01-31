#inputs
name=input("Enter your name: ")
course=input("Enter your course: ")
year_sec=input("Enter your year and section: ")
acadyear=input("Enter your academic year: ")
fnum=int(input("Enter your first number: "))
snum=int(input("Enter second number: "))

#operations
sum = fnum + snum
difference = fnum - snum
product = fnum*snum 
quotient= fnum/ snum

#prints
print("The sum of",fnum, "and",snum, "is",sum)
print("The difference of" , fnum, "and", snum , "is", difference)
print("The product of", fnum, "and", snum, " is", product) 
print("The quotient of", fnum, "and", snum, "is", quotient)
print("My name is ", name, course, year_sec, "A.Y.", acadyear)
    