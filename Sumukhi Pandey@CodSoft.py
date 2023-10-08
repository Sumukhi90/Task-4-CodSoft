# Rock-Paper-Scissors Game
User Input: Prompt the user to choose rock, paper, or scissors.
Computer Selection: Generate a random choice (rock, paper, or scissors) for
the computer.
Game Logic: Determine the winner based on the user's choice and the
computer's choice.
Rock beats scissors, scissors beat paper, and paper beats rock.
Display Result: Show the user's choice and the computer's choice.
Display the result, whether the user wins, loses, or it's a tie.
Score Tracking (Optional): Keep track of the user's and computer's scores for
multiple rounds.
Play Again: Ask the user if they want to play another round.
User Interface: Design a user-friendly interface with clear instructions and feedback.

import random
boolValue=True
userScore, computerScore=0,0
while boolValue:
    print("ROCK PAPER OR SCISSORS?")
    options=["rock","paper","scissors"]
    computerChoice=random.randint(1,3)
    userChoice=int(input("Enter 1 for rock\nEnter 2 for paper\nEnter 3 for scissors\nEnter 4 if you want to exit the game"))
    if userChoice == 4:
        boolValue=False
    elif userChoice==computerChoice:
        print(f"Its a draw! You both chose {options[userChoice-1]}.")
    else:
        if userChoice==computerChoice-1:
            print(f"You lost! You chose {options[userChoice-1]} and computer chose {options[computerChoice-1]}.")
            computerScore+=1 
        elif userChoice==3 and computerChoice==1:
            print(f"You lost! You chose {options[userChoice-1]} and computer chose {options[computerChoice-1]}.")
            computerScore+=1
        else:
            print(f"You won You chose {optional[userChoice-1]} and computer chose {options[computerChoice-1]}.")
            userScore+=1
if userScore>computerScore:
    print(f"CONGRATS! YOU WON THE GAME!\nYou-{userScore}:Computer-{computerScore}")
elif userScore<computerScore:
    print(f"BETTER LUCK NEXT TIME! YOU LOST THE GAME!\nYou-{userScore}: Computer-{computerScore}")
else:
     print(f"THE GAME ENDS IN A DRAW!\nYou-{userScore} : Computer-{computerScore}")  
                         
                         
