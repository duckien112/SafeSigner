#number = '457891236'
#password = '1234'
#seeds = 'a1 b2 c3 d4 e5 f6 g7 h8 i9 j10 k11 l12'
from lib import *

action = input("If encrypt enter 1, else 0: ")
number = input("Enter number with 9 chars in Visa: ")
seeds = input("Enter seeds: ")

print(changeSeeds(seeds, number, action))