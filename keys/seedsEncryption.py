#number = '457891236'
#password = '1234'
#seeds = 'a1 b2 c3 d4 e5 f6 g7 h8 i9 j10 k11 l12'
from lib import *
import getpass

#action = getpass.getpass("If encrypt enter 1, else 0: ")
while True:
    action = getpass.getpass("If encrypt enter 1, else 0: ")
    if action == "0" or action == "1":
        break
    else:
        print("Only 0 or 1")
        
if action == "1":
    while True:
        number = getpass.getpass("Enter number with 9 chars in Visa: ")
        number1 = getpass.getpass("Renter number with 9 chars in Visa: ")

        if number == number1:
            break
        else:
            print("Number not match!!!")
            
    while True:
        password = getpass.getpass("Enter word with 9 chars in Visa: ")
        password1 = getpass.getpass("Renter word with 9 chars in Visa: ")

        if password == password1:
            break
        else:
            print("Password not match!!!")
else:
    number = getpass.getpass("Enter number with 9 chars in Visa: ")
    password = getpass.getpass("Enter word with 9 chars in Visa: ")
    
seeds = getpass.getpass("Enter seeds: ")

print(encryptSeeds(action, number, password, seeds))
