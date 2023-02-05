
# 10. Create a class BANK and with two function simple interest and compound interest. 
#  U need to create instance for pnb, icici and hdfc banks with corresponding input.

class BANK:
    def __init__(self, principle, rate, time):
        self.Principle = principle
        self.Rate = rate
        self.Time = time

    def simpleInterest(self):
        Amount =  (self.Principle*self.Rate*self.Time)/100
        return Amount

    def compoundInterest(self):
        Amount = self.Principle*(pow((1 + self.Rate/100), self.Time)) - self.Principle
        return Amount

bName = input("Please Enter your Bank Name pnb/icici/hdfc: ")
principle = int(input("Please enter your principle amount: "))
rate = int(input("please enter rate: "))
time = int(input("Please enter time: "))

if(bName == "pnb"):
    pnb = BANK(principle, rate, time)
    print("PNB simple inerest: ", pnb.simpleInterest())
    print("PNB compound inerest: ", pnb.compoundInterest())
elif(bName == "icici"):
    icici = BANK(principle, rate, time)
    print("ICICI simple inerest: ", icici.simpleInterest())
    print("ICICI compound inerest: ", icici.compoundInterest())
elif(bName == "hdfc"):
    hdfc = BANK(principle, rate, time)
    print("HDFC simple inerest: ", hdfc.simpleInterest())
    print("HDFC compound inerest: ", hdfc.compoundInterest())
else:
    print("you enter invalid bank name please try again !!!")