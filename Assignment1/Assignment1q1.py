# Q1. print number is prime or not *****************************
def prime(num):
    for i in range(2, num):
        cnt=0;
        for j in range(2, i):
            if(i%j==0):
                cnt+=1;
        if(cnt<1):
            print(i)

num = int(input("Please enter your number: "))
prime(num)
