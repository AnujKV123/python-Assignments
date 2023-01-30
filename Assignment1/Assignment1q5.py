# india(m-18,f-18), srilanka(m-18,f-21), saudi(m-18,f-cant) conditions to write the functionality

def checkElagible(age, gender, country):
    if country == "india":
        if gender=="m" or gender=="f":
            if age >= 18:
                print("Elagible")
            else:
                print("not Elagible")
        else:
            print("you entered wrong gender! please try again!!")

    elif country == "srilanka":
        if gender == "m":
            if(age>=18):
                print("Elagible")
            else:
                print("Not Elagible")

        elif gender == "f":
            if(age>=21):
                print("Elagible")
            else:
                print("not Elagible")
        else:
            print("you entered wrong gender! please try again!!")

    elif country == "saudi":
        if gender == "m":
            if age>=18:
                print("Elagible")
            else:
                print("not Elagible")

        else:
            print("not Elagible")

    else:
        print("you enterde wrong country name! please try again!!!!!")



country = input("Please enter your country name: ")
gender = input("please enter your gender: ")
age = int(input("please enter your age: "))

checkElagible(age, gender, country)