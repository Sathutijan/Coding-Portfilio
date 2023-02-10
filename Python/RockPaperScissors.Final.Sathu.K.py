from random import randint  # Importing randint function from random module
from time import sleep      # Importing sleep function from time module
import sys                  # Importing sys module

# File Name: RockPaperScissors.Final.Sathu.K.py
#
# Author: Sathu. K
#
# Date: Jan 5th, 2021
#
# Description: This is a simulation of a game of rock, paper scissors.
#              The user first inputs either rock, paper or scissors into the program.
#              The program then randomly generates 1, 2, or 3 which correlates to a
#              sign in rock, paper, scissors. Then program determines if the user or
#              the computer wins. The user and the computer both have 3 lives each. Every
#              time the user or the computer loses, they get lose a life. Everytime
#              the user or the computer wins they gain a life. The game ends when
#              either the user or the computer runs out of lives.
#

# Greeting message to display on screen
greetingMessage = "\nWelcome to a game of Rock, Paper, Scissors!\n"
   
for char in greetingMessage:                                            # Every character stored in the greetingMessage variable
    sys.stdout.write(char)                                              # is printed on screen with a 0.1 seconds delay
    sys.stdout.flush()                                                  # using sys module and sleep function from time module.
    sleep(0.1)

# Ask user if they would like to start the game
restart = input("(Enter any key to start the game) or (Enter \"no\" to end game): ")

# A variable which stores a line to separate text
line = "======================================================="

# The rules of the game are printed on screen
print(line)
print("RULES OF THE GAME")

# All the rules of the game are stored in a variable known as "rules"
rules = ("\nThe Rules of the Rock, paper, scissors game as follows: \n"
         + "\n1.The computer and user has 3 lives each\n"
         + "\n2.The winner of each round gains a life\n"
         + "\n3.The loser of each round loses a lfe\n"
         + "\n4.First one to reach 0 lives loses the game\n"
         + "\n5.The game will end when either computer or user has 0 lives left\n"
         + "\n6.The following combinations determine who wins:\n"
         + "\n -Rock versus paper, paper wins \n"
         + " -Scissor versus rock, Rock wins \n"
         + " -Paper versus scissor, scissor wins \n"
         + " -If both user and computer choose the same move, it's a tie\n"
         + "\n7. Keep in mind that this game is case sensitive (Enter Lowercase only)\n")

for char in rules:                                                      # Every character stored in the rules variable
    sys.stdout.write(char)                                              # is printed on screen with a 0.03 seconds delay
    sys.stdout.flush()                                                  # using sys module and sleep function from time module.
    sleep(0.03)

print(line)                                                             # printing line to separate text

print("\nROUND 1 WILL BEGIN IN 5 SECONDS!")                             # A message will be printed on screen letting user
                                                                        # know that round will start soon

for i in range(5, 0, -1):                                               # Using for loop, program will count down from 5
    print(i)                                                            # to 0 with a 1-second delay using sleep
    sleep(1)                                                            # function from time module

# While restart is anything other than "no" the program will run the loop
while restart != "no":

    # Amount of lives user and computer have
    userLives = 3
    computerLives = 3

    # A variable to store the amount of rounds played
    round = 0

    # While the user lives and computer lives is greater than 0 the loop will run
    while userLives and computerLives > 0:

        # Line to separate text and make it look organized
        print(line)

        # A round is added everytime the loop runs
        round = round + 1

        # prints the amount of rounds played
        print("ROUND " + str(round))

        # While the user enters anything other than rock, paper and scissors, the program will display an error message
        # and will continuously loop until the if condition is false
        while True:

            # Prompt user to input either Rock, Paper, or Scissors
            userPick = input("\nPlease enter \"rock\",\"paper\", or \"scissors\": ")

            if userPick != "rock" and userPick != "paper" and userPick != "scissors":
                print("That is not a valid choice. Please try again: ")
                print(line)
            else:
                break


        delayMessage = "\nLoading...\n"                                 # A variable which stores "Loading..."


        def loading():                                                  # it creates a function that stores a series of code
                                                                        # allowing me to repeat this code whenever "loading()"
                                                                        # is written

            for char in delayMessage:                                   # Every character stored in the variable
                sys.stdout.write(char)                                  # is printed with a 0.2 seconds delay each time
                sys.stdout.flush()                                      # using sys module and sleep function from time module.
                sleep(0.2)


        loading()                                                       # This loading variable is an indicator to run the code
                                                                        # stored in the variable



        # A random number between 1 and 3 is generated using randint function.
        # 1 is rock, 2 is paper and 3 is scissors.
        computerPick = randint(1, 3)


        # Program determines if user or computer wins
        if computerPick == 1:

            if userPick == "rock":                                      # If the computer picks rock and user picks rock
                print("\nYou and the computer chose rock")              # the program will display "Tie!" and a message
                print("Tie!")                                           # saying that "Nobody has lost a life".
                print("\nNobody has lost a life")


            elif userPick == "paper":                                   # If computer picks rock and user picks paper
                print("\nYou chose paper, the computer chose rock")     # the program will display "You Win!"
                print("You win!")
                userLives = userLives + 1                               # User gains a life when they win
                computerLives = computerLives - 1                       # Computer loses life when they lose

            else:                                                       # Else the computer picks rock and user picks
                print("\nYou chose scissors, the computer chose rock")  # scissors program will display "You Lose!"
                print("You Lose!")
                userLives = userLives - 1                               # User loses a life when they lose
                computerLives = computerLives + 1                       # Computer gains life when they win

            # Prints the amount of lives computer and user has left
            print("\nYou have", userLives, "lives left")
            print("The computer has", computerLives, "lives left")


        elif computerPick == 2:

            if userPick == "rock":                                      # If computer picks paper and user picks rock
                print("\nYou chose rock, the computer chose paper")     # the program will display "You Lose!"
                print("You Lose!")
                userLives = userLives - 1                               # User loses a life when they lose
                computerLives = computerLives + 1                       # Computer gains a life when they win

            elif userPick == "paper":                                   # If computer picks paper and user picks paper
                print("\nYou and the computer chose paper")             # the program will display "Tie!" and a message
                print("Tie!")                                           # saying that "Nobody has lost a life".
                print("\nNobody has lost a life")

            else:                                                       # Else the computer picks paper and user picks
                print("\nYou chose scissors, the computer chose paper") # scissors program will display "You Win!"
                print("You Win!")
                userLives = userLives + 1                               # User gains a life when they win
                computerLives = computerLives - 1                       # Computer loses a life when they lose

            # Prints the amount of lives computer and user has left
            print("\nYou have", userLives, "lives left")
            print("The computer has", computerLives, "lives left")


        else:

            if userPick == "rock":                                      # If the computer picks scissors and user picks
                print("\nYou chose rock, the computer chose scissors")  # rock the program will display "You Win!"
                print("You Win!")
                userLives = userLives + 1                               # User gains a life when they win
                computerLives = computerLives - 1                       # Computer loses a life when they lose

            elif userPick == "paper":                                   # If the computer picks scissors and the user
                print("\nYou chose paper, the computer chose scissors") # picks paper the program will display "You Lose"
                print("You Lose!")
                userLives = userLives - 1                               # User loses a life when they lose
                computerLives = computerLives + 1                       # Computer gains a life when they win

            else:                                                       # Else the computer picks scissors and the user
                print("\nYou and the computer chose scissors")          # pick scissors the program will display
                print("Tie!")                                           # "Tie!" and a message that "Nobody has lost a
                print("\nNobody has lost a life")                       # life".

            # Prints the amount of lives computer and user has left
            print("\nYou have", userLives, "lives left")
            print("The computer has", computerLives, "lives left")


    # Line to separate text and make it look organized
    print(line)

    if userLives == 0:                                                  # If user has 0 lives left the program will
        print("\nSorry you have run out of lives! YOU LOSE!")           # display the following message

    else:                                                               # Else computer has 0 lives left the program will
        print("\nThe computer has run out of lives! YOU WIN!")          # display the following message

    # Asking user whether they would like to play again
    restart = input(
        "\nWould you like to restart the program?\n(Enter \"no\" to end the game or Enter any key to restart the game): ")

    # If user enters "no" the program will stop. If they do not the program will continue the loop
    if restart == "no" or restart == "No":
        print("\nThank you for playing my game of Rock, Paper, Scissors!")
        break

    # If user enters anything other than "no" then the program will loop back to the start with a loading message
    else:
        loading()

# Line to separate text and make it look organized
print(line)

# Output message when user ends the game or does not want to restart.
print("You have successfully exited the game!")
