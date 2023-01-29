# Q2. check number is even or odd ********************************************

def oddEven(n):
    if(num%2 == 0):
        print(f"{num} is a Even Number")
    else:
        print(f"{num} is a Odd Number")

num = int(input("Please Enter your Number: "))
oddEven(num)