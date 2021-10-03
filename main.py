
#/////////////////////////////////////////////////////
#
# Type : Terminal based app
# Made by Nayzalix for mastering Python
#
#/////////////////////////////////////////////////////


#----Modules----#
from pycenter import center


#----Ascii Thing----#
title = """

     _____                      __            __    __ 
    / ___/__  ___ _  _____ ____/ /____ ______/ /___/ /_
   / /__/ _ \/ _ \ |/ / -_) __/ __/ -_) __/_  __/_  __/
   \___/\___/_//_/___/\__/_/  \__/\__/_/   /_/   /_/   
<-------------------------------------------------------->
                                                    
"""
opt = """
[1] Convert Fahrenheit to Celsius   |    [3] Euro to Dollar
[2] Convert Celsuis to Fahrenheit   |    [4] Dollar to euro
"""

print(center(title))
print(opt)


#----Convertion Function----#
def FtoC(Faren):
    Celsius = (Faren - 32) * 5/9
    print(Celsius)

def CtoF(Cels):
    faren = Cels * 9/5 + 32
    print(faren)

def EurToDol(euro):
    dol = euro * 0.86
    print(f"[!] Around {dol} Dollars")

def DolToEur(dollar):
    eur = dollar * 1.16
    print(f"[!] Around {eur} Euros")
#----Variables----#
count = 0

#----Main code----#
while True:
    choice = input("Choose a option -> ")
    try:
        if choice == "1":
            FtoC(int(input("Enter a fahrenheit value -> ")))
            
        elif choice == "2":
            CtoF(int(input("Enter a Celsius value -> ")))
        
        elif choice == "3":
            EurToDol(int(input("Enter Your value -> ")))

        elif choice == "4":
            DolToEur(int(input("Enter Your value -> ")))

        elif choice == "":
            print("Really !! Man ! No jsut choose one option above\n")
            count += 1
        else:
            print("You are choosing an option that doesn't exist or not implemented Yet")
            
    except Exception as e:
        print(f"[!]Warning !! An error was found during the execution of the script -> {e}")

    if count == 2:
        print("Are you dumb !!\n")
    elif count == 3:
        print("Close this terminal bro please, for everyone !\n")
    elif count == 20: 
        print("Ok i close it for you\n")
        break