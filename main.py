#file where we pull all of the games together into one file that makes 
#it run
import madlibs as m
import rock_paper_scissors as r
from guess_the_number import Gooberville as g
import time as t

def pa():
    pin = input("Would you like to select a new game?\n y/n>>>")
    if pin == 'y' or pin == 'Y':
        print("loading...")
        t.sleep(2)
        GetGame()
    elif pin == 'n' or pin == 'N':
        t.sleep(1)
        print("See Ya!")
        ...
    else: 
        print("Invalid Response...")
        pa()

def GetGame():
    fc = input("What game would you like to play?\n 1. madlibs\n 2. Guess the Number! \n 3.Rock paper scissors \n>>> ")
    if fc == '1':
        m.madlibmain()
        pa()
    elif fc == '2':
        g().GTN()
        pa()
    elif fc == '3':
        r.RockPaperScissors()
        pa()
    else:
        print("Invalid Response")
        GetGame()


GetGame()