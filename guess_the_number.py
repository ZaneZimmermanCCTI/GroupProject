import random as rd
import time as t

class Gooberville:
    youareabuffoon = rd.randint(1,20)
    lives = 3
    playerguess = None

    def Guess(self):
        try: 
            self.playerguess = int(input("Please enter a number from 1 to 20>>>"))
        except:
            print("Invalid Response, try again...")
            self.lives += 1

    def PlayAgain(self):
        p = input('Would you like to play again? \n y/n>>>')
        if p == "y" or p == "Y":
            print("You're the boss!")
            self.GTN()
        else: 
            ...

    def LifeChk(self):

        if self.lives == 3:
            print("You have 3 guesses!")
        elif self.lives == 2:
            print("Oof... looks like you guessed wrong. \n 2 guesses left...")
        elif self.lives == 1:
            print("Last guess! choose wisely...")
        else:
            print("You Lose!")
            t.sleep(3)
            self.lives = 3
            self.PlayAgain()


    def GTN(self):
        print("Let's see if you can guess the number!")
        self.LifeChk()
        self.Guess()
        if self.playerguess == self.youareabuffoon:
            print("We have a winner!")
            self.PlayAgain()
        else:
            self.lives -= 1
            self.GTN()


