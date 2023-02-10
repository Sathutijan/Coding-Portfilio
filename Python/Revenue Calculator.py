# Author: Sathu.K
#
# Date: November 25, 2021
#
# Description:  The program asks the user for number of adults and kids(under 16)
#               attending the play for a night. If the value entered ia negative
#               the program will display an error message. If not Using the input,
#               the program will calculate the revenue based on the number of tickets sold.
#               Then, the program will determine if the revenue created is a loss or profit
#               by subtracting the revenue by the expenses of play for a day ($5000)
#               and displays the result and it’s amount on screen to the user. If user desires a
#               second night the program will repeat but the expenses will be 2500$.
#               Finally, the program will add the profit/loss of both nights and display
#               it on screen to the user.
#


while True:

# Prompt user to enter the number of adults and kids attending for night 1

    numberOfKids = int(input("\nPlease enter the amount of kids attending night 1: "))
    numberOfAdults = int(input("Please enter the amount of adults attending night 1: "))

    expenses = int(5000)                                            # Expense of play for 1st night



# Error message if a negative number is entered for night 1

    if numberOfKids < 0 or numberOfAdults < 0:
        print("Error! Please Try again")
        numberOfKids = int(input("Please enter a positive amount of kids attending : "))
        numberOfAdults = int(input("Please enter positive amount of adults attending : "))

    

# Calculate revenue based on amount of adults and kids attending

    revenueFromKids = int(numberOfKids) * 9.99                       # The price of a ticket for kids (under 16) is $9.99
    revenueFromAdults = int(numberOfAdults) * 15.99                  # The price of a ticket for adults is $15.99
    totalRevenue = revenueFromAdults + revenueFromKids  



# Create Output message to display

    outputProfit1 = "\nThe total revenue from night one play has lead to a Profit of: ${:.2f}"
    outputLoss1 = "\nThe total revenue from night one play has lead to a Loss of: ${:.2f}"     
    outputProfit2 = "\nThe total revenue from night two play has lead to a Profit of: ${:.2f}"
    outputLoss2 = "\nThe total revenue from night two play has lead to a Loss of: ${:.2f}"
    outputProfitTotal = "\nThe total revenue from both plays together has lead to a overall profit of: ${:.2f}"
    outputLossTotal = "\nThe total revenue from both plays together has lead to a overall loss of: ${:.2f}"



# Determine if the revenue created is a profit or loss

    if totalRevenue > expenses:                                      # Determine if there was profit or not
        profitLoss = totalRevenue - expenses                         # Calculating amount of profit
        print(outputProfit1.format(profitLoss))                      # Output Message


    else:
        profitLoss = (totalRevenue - expenses) * -1                  # Calculating amount of Loss
        print(outputLoss1.format(profitLoss))                        # Output Message

    

# Determining if user would like a second night

    nights = input("\nWill you like a another night of the play? Yes or No: ")  


    if nights == "yes" or nights == "Yes":                           # If user wants another night program
        expenses2 = int(2500)                                        # Expense of play for 2nd night


        numberOfKids = int(input("\nPlease enter the amount of kids attending night 2: "))
        numberOfAdults = int(input("Please enter the amount of adults attending night 2: "))


    elif nights == "no" or nights == "No":                           # If user does not want another night program will
        repeat = input("\nWould you like to restart the program: ")  # Asking if user wants to restart the program

        if repeat == "yes" or repeat == "Yes":                       # If answer is yes the program will restart
            continue

        elif repeat == "no" or repeat == "No":                       # If answer is no the program will stop
            print("\nThank you for using our program goodbye!")
            break
   

# Error message if user enters a negative number for night 2

    if numberOfKids < 0 or numberOfAdults < 0:
        print("\nError! Please Try again")
        numberOfKids = int(input("\nPlease enter a positive amount of kids attending : "))
        numberOfAdults = int(input("Please enter positive amount of adults attending : "))



# Calculate revenue based on amount of adults and kids attending

    revenueFromKids = int(numberOfKids) * 9.99                       # The price of a ticket for kids (under 16) is $9.99
    revenueFromAdults = int(numberOfAdults) * 15.99                  # The price of a ticket for adults is $15.99
    totalRevenue2 = revenueFromAdults + revenueFromKids


    expenses2 = int(2500)                                            # Expenses for second night


    if totalRevenue2 > expenses2:                                    # Determine if there was profit or not
        profitLoss2 = totalRevenue2 - expenses2                      # Calculating amount of profit
        print(outputProfit2.format(profitLoss2))                     # Output Message


    else:
        profitLoss2 = (totalRevenue2 - expenses2) * -1               # Calculating amount of Loss
        print(outputLoss2.format(profitLoss2))                       # Output Message



# Asking if user wants a total profit/loss from both nights together

    total = input("\nDo you want a total loss/profit of both nights? Yes or No: ")


    if total == "yes" or total == "Yes":                             # If the answer is yes the program will continue                                                     
        wholeRevenue = totalRevenue + totalRevenue2                
        totalExpenses = expenses + expenses2


        if wholeRevenue > totalExpenses:                             # Determine if there was profit or not overall
            totalProfitOrLoss = wholeRevenue - totalExpenses         # Calculating amount of profit
            print(outputProfitTotal.format(totalProfitOrLoss))       # Output Message


        else:
            totalProfitOrLoss = (wholeRevenue - totalExpenses) * -1  # Calculating amount of Loss
            print(outputLossTotal.format(totalProfitOrLoss))         # Output Message


            repeat = input("\nWould you like to restart the program: ") # Asking if user wants to restart the program

            if repeat == "yes" or repeat == "Yes":                      # If answer is yes the program will restart
                continue

            elif repeat == "no" or repeat == "No":                      # If answer is no the program will stop
                print("\nThank you for using our program goodbye!")
                break

    elif total == "no" or total == "No":                                
        repeat = input("\nWould you like to restart the program: ")

        if repeat == "yes" or repeat == "Yes":                          # If answer is yes the program will restart
            continue

        elif repeat == "no" or repeat == "No":                          # If answer is no the program will stop
            print("\nThank you for using our program goodbye!")
            break
