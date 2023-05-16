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
    
    if playerinput == urmom:
        print("You done be committed to a tie...")
        PlayAgain()
    elif playerinput == "rock" and urmom == "paper":
        print(f'Player Choice: {playerinput}! \nComputer choice: {urmom}!')
        print("Computer Wins.")
        PlayAgain()
    elif playerinput == "paper" and urmom == "rock":
        print(f'Player Choice: {playerinput}! \nComputer choice: {urmom}!')
        print("Player Wins.")
        PlayAgain()
    elif playerinput == "scissors" and urmom == "rock":
        print(f'Player Choice: {playerinput}! \nComputer choice: {urmom}!')
        print("Computer Wins.")
        PlayAgain()
    elif playerinput == "rock" and urmom == "scissors":
        print(f'Player Choice: {playerinput}! \nComputer choice: {urmom}!')
        print("Player Wins.")
        PlayAgain()
    elif playerinput == "paper" and urmom == "scissors":
        print(f'Player Choice: {playerinput}! \nComputer choice: {urmom}!')
        print("Computer Wins.")
        PlayAgain()
    elif playerinput == "scissors" and urmom == "paper":
        print(f'Player Choice: {playerinput}! \nComputer choice: {urmom}!')
        print("Player Wins.")
        PlayAgain()

    
        
         
