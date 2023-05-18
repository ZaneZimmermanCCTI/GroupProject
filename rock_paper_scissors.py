import random as r

def PlayAgain():
    pin = input("Would you like to play again? \n y/n>>>")
    if pin == "y" or pin == "Y":
        RockPaperScissors()
    elif pin == "n" or pin == "N":
        print("returning to main menu...")
     
def RockPaperScissors():
    urmom = r.randint(1,3) 
    if urmom == 1:
        urmom = "rock"
    elif urmom == 2:
        urmom = "paper"
    elif urmom == 3:
        urmom = "scissors"

    playerinput = int(input("Please enter an item:\n 1.Rock \n 2.Paper \n 3.Scissors \n>>>"))
    if playerinput == 1:
        playerinput = 'rock'
    elif playerinput == 2:
        playerinput = 'paper'
    elif playerinput == 3:
        playerinput = 'scissors'
    else: 
        print("Invalid input.")
        RockPaperScissors()
    
    print(f"Your choice: {playerinput}\nComputer's choice: {urmom}")
    if playerinput == "rock" and urmom == "paper" or playerinput == "scissors" and urmom == "rock" or playerinput == "paper" and urmom == "rock":
        print("You win!")

    else:
        print("You lose!")
    
    PlayAgain()

    
        
         
