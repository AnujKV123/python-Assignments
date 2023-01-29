import calculatorProgram as c

def Calculator(a, b):
    print("sum of a and b = ", c.add(a, b))

    print("minus of a and b = ", c.minus(a, b))

    print("multiplication of a and b = ", c.product(a, b))

    print("devesion of a and b = ", c.devide(a, b))

    print("modulas of a and b = ", c.modulas(a, b))

a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))
Calculator(a,b)