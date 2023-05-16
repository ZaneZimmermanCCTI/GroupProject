import random as rd
import time as t

def PlayAgain():
    p = input('Would you like to play again? \n y/n>>>')
    if p == "y" or p == "Y":
        print("You're the boss!")
        oof()
    else: 
        ...

def oof():
    youareabuffoon = rd.randint(1,20)
    playerguess1 = int(input("Enter a number from 1 to 20>>>"))
    if playerguess1 == youareabuffoon:
        t.sleep(3)
        print('YOU IS BE IS A WINNER!!!')
        PlayAgain()
        
    else: 
        print("Wrong ya goober")
        t.sleep(3)
        print("2 lives left...")
        t.sleep(1)
        playerguess2 = int(input("Enter another number from 1 to 20, except for the number you selected previously.>>>"))
        if playerguess2 == youareabuffoon:
            t.sleep(3)
            print('YOU IS BE IS A WINNER!!! on the second try...')
            PlayAgain()

        else:
            print("Wrong number again ya goobis")
            t.sleep(3)
            print("only one life left... be careful!")
            t.sleep(2)
            playerguess3 = int(input("Enter another number from 1 to 20, except for the two numbers you selected previously.>>>"))
            if playerguess3 == youareabuffoon:
                t.sleep(3)
                print("WHAT A GAME!!! Cuttin' it close with the last-life guess!")
                PlayAgain()
            else:
                print("Oof, it looks like you are tonight's big loser!")
                t.sleep(2)
                PlayAgain()
                
    
