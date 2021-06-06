import random
import time
import os
def cls():

  os.system('cls' if os.name=='nt' else 'clear')

cls()
a = """

░█████╗░░█████╗░███╗░░██╗░██████╗░█████╗░██╗░░░░░███████╗  ░██████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░░░███████╗
██╔══██╗██╔══██╗████╗░██║██╔════╝██╔══██╗██║░░░░░██╔════╝  ██╔════╝░██╔══██╗████╗░████║██╔══██╗██║░░░░░██╔════╝
██║░░╚═╝██║░░██║██╔██╗██║╚█████╗░██║░░██║██║░░░░░█████╗░░  ██║░░██╗░███████║██╔████╔██║██████╦╝██║░░░░░█████╗░░
██║░░██╗██║░░██║██║╚████║░╚═══██╗██║░░██║██║░░░░░██╔══╝░░  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══██╗██║░░░░░██╔══╝░░
╚█████╔╝╚█████╔╝██║░╚███║██████╔╝╚█████╔╝███████╗███████╗  ╚██████╔╝██║░░██║██║░╚═╝░██║██████╦╝███████╗███████╗
░╚════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░░╚════╝░╚══════╝╚══════╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚══════╝
                                   Author: @Callistodev1, Pulatov Kamran
"""
print(a)
a = int(input("Your bet: "))
b = int(input("Enter all options(integer): "))
try:
    z = (1 / (b)) * 100
    print("Win percent: " + str(round(z)) + "%")
except:
    print("Math error! please try again")
    quit()
if b == 1:
    print("Error! Winning option more than all options")
    quit()
def prise():
    if b + 1 == 3:
        cash = 10 + a
        print("Your cash: " + str(cash) + "$")

    elif b + 1 > 3:
        cash = 30 + a
        print("Your cash: " + str(cash) + "$")
print("Waiting...")
time.sleep(2)        
x = random.randrange(1, b+1)
if x == 1:
    print("Result: " + str(x))
    prise()
    print("You win!!!")
else:
    print("Result: " + str(x))
    print("Cash: " + str(a - 5))
    print("You lose")


