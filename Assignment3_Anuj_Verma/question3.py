
# 3. convert a number into binary and binary to number.

def numberToBinary(val):
    binaryX = ""
    x = val
    while(val>0):
        if val%2==0:
            binaryX += "0"
        else:
            binaryX += "1"
        val = val//2
    finalBinary = binaryX[::-1]
    print(f"Binary of {x}: {finalBinary}")
    binaryToNumber(int(finalBinary))


def binaryToNumber(val):
    b = val
    number = 0
    power = 1
    while val>0:
        reminder = val%10
        val = val//10
        number += reminder*power
        power = power*2
    print(f"Decimal of {b}: {number}")

val = int(input("Enter Your Number: "))
numberToBinary(val)