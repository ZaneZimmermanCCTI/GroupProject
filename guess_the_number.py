import random as rd
import time as t

lives = 3
youareabuffoon = rd.randint(1,20)


def PlayAgain():
    p = input('Would you like to play again? \n y/n>>>')
    if p == "y" or p == "Y":
        print("You're the boss!")
        GTN()
    else: 
        ...

def LifeChk():
    if lives == 3:
        print("You have 3 guesses!")
    elif lives == 2:
        print("Oof... looks like you guessed wrong. \n 2 guesses left...")
    elif lives == 1:
        print("Last guess! choose wisely...")
    else:
        print("You Lose!")
        t.sleep(3)
        lives = 3
        PlayAgain()


def GTN():
    print("Let's see if you can guess the number!")
    LifeChk()
    playerguess = int(input("Enter a number from 1 to 20>>>"))
    if playerguess == youareabuffoon:
        print("We have a winner!")
        lives = 3
        PlayAgain()
    else:
        GTN()


                
    
