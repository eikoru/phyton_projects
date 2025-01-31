def main():
    name= input("Input your name: ")
    while True:
        math=int (input("enter your math grade: "))
        english= int (input("enter your english grade: "))
        filipino= int(input("enter your filipino grade: "))
        average=(math + english + filipino)/3

        if average >=75:
            print("your average grade is" ,average, "you passed!")
        else: 
            print("your average grade is" ,average, "you failed")
    
        repeat=input("Do you want to try again? ")
        if repeat == "yes" or 'y':
            main()
        else: 
            print("thank you, have a nice day")
            break
main()