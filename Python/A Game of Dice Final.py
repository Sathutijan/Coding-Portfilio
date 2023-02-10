from random import randint # Importing the randit function from random library
# Author: Sathu. K
#
# Date: December 8th, 2021
#
# Description: The program randomly generates 2 different numbers between
#              1 and 6 using the randint function. The 2 numbers act as 
#              dice. After the 2 numbers are generated the sum of both
#              numbers is calculated. If the sum of both these equals to
#              7 the user wins the game. If the sum does not equal to
#              7 the user loses the game.
#

def restart():

    # Greeting message to user
    print("\nWelcome to a Game of Dice.")
    print("The objective of this game is to roll 2 dice with the sum of 7")      # message stating objective of game.
    print("--------------------------------------")                              # Line to seperate text

    # Asking user if they would like to start the game
    start = input("Press Enter to start the game: ")

    start = "y"
    lives = 10                                                                   # Amount of lives
    rounds = 1                                                                   # A variable to determine how many rounds are played

    while start == "y" and lives > 0:                                            # The program will loop as long as start equals "y"

        print("\nROUND " + str(rounds))                                          # Display the number of rounds
        
        myDie1Roll = randint(1,6)                                                # Generates random number from 1 to 6 for dice 1 using randint
        print("\nThe first dice rolled a: " + str(myDie1Roll))                   # Display the number generated for dice 1 on screen
        
        myDie2Roll = randint(1,6)                                                # Generates random number from 1 to 6 for dice 2 using randint
        print("The second dice rolled a: " + str(myDie2Roll))                    # Display the number generated for dice 2 on screen    

        totalDice = myDie1Roll + myDie2Roll                                      # Calculates the sum of dice 1 and dice 2
        print("The sum of both dice is: " + str(totalDice))                      # Display total sum of both dice on screen


        if totalDice == 7:                                                       # If the sum of both dice is 7 the program will
            lives = lives + 1                                                    # display that the user has won the game and will
            print("\nCongrats you win! You have sucessfully beat the computer")  # add a additional life and display lives on screen
            print("You have " + str(lives) + " lives left." )

        else:                                                                    # If the sum of both dice is anything else other
            lives = lives - 1                                                    # then 7 the program will display that the user
            print("\nSorry! the computer beat you. Try harder next time")        # has lost the game and will remove a life and display
            print("You have " + str(lives) + " lives left.")                     # remaining lives left on screen

        
        
        while lives > 0:                                                         # While the number of lives is greater then 0
            start = input("\nWould you like to another round? \"y\" or \"n\": ") # the program will ask the user if they would play
                                                                                 # another round.

            rounds = rounds + 1                                                  # Adds a round every time the dice is rolled                                                                            
                                                                                 
            if start == "n":                                                     # If the user answers "n" the program will print
                print("\nThank you for playing a Game of Dice! Goodbye")         # "thank you for playing a game of dice"
                exit()

            elif start == "y":                                                   # If the user answers "y" the program will go back to the start
                print("--------------------------------------")                  # Line to seperate text
                break

            else:                                                                # If the user answers anything other then "y" or "n" the
                print("\nInvaild Input! Enter \"y\" or \"n\": ")                 # program will display a error message.

    print("\nGAME OVER!")                                                        # If user has 0 lives left the program will display game over
    print("You have survived till round " + str(rounds))                         # and the amount of rounds survived

    while lives == 0:
    
        start = input("\nWould you like to restart the game? \"y\" or \"n\": ")  # Asking user if they would like to restart the game.

        if start == "y":                                                         # If user answers "y" program will restart from the very
            restart()                                                            # beginning.

        elif start == "n":                                                       # If user answers "n" program will display a goodbye message
            print("Thank you for playing a Game of Dice! Goodbye")               # and will exit the program.    
            exit()

        else:                                                                    # If user enter anything else other then "y" or "n" program                    
            print("Invaild Input! Enter \"y\" or \"n\": ")                       # will display error message
             
restart()
