def cost_of_food():
    # while loop exists so if user input is invalid, the code can reloop back to acquire valid input.
    while True:
        try:
            # Asking for the user to input the amount of their subtotal and converting to a float
            subtotal = input(
                "What was the total cost of your meal before taxes? (The format should be ##.##)"
            )
            subtotal = float(subtotal)
            # subtotal must be return a positive number, therefore the code reasks user to re-enter if a negative number is input
            if subtotal >= 0:
                return subtotal
            else:
                continue
        # if the user puts text or symbols that can't convert to a float, the except handles the error
        except ValueError:
            # If the input subtotal is not valid, we're asking the user to try again (It prints then loops back to try above)
            print("Please check your entry and try again.")


def add_tip():
    # while loop is needed to validate the user's input
    while True:
        try:
            # Requesting user input a percent tip
            tip_percent = input("What percent tip do you wish to give your server? ")
            tip_percent = float(tip_percent)
            # tip percent must be positive, so if user inputs a negative number, a comment is given and then looped back to the bginning
            if tip_percent < 0:
                print("Stop trying to break my code. It won't work.")
                continue
            # just comments on the user's generosity -- this is merely for my own satisfaction
            elif tip_percent == 0:
                print("You're a jerk")
            elif 0 < tip_percent < 15:
                print("Was the service bad or are you just being greedy?")
            else:
                print("I'm sure your server will be grateful")
            # if tip_percent meets all the above qualifications, it is output from the function.
            return tip_percent
        # If the input subtotal is not valid, we're asking the user to try again (It prints then loops back to try above)
        except ValueError:
            print(
                "That input was not valid. What percent tip do you wish to give your server? "
            )


def split_bill():
    # while loop is needed to validate the user's input
    while True:
        try:
            # Requesting user input the number of people splitting the bill
            num_of_people = input("How many people are splitting the bill? ")
            num_of_people = int(num_of_people)
            #The number of people must be non-zero (to not crash the code because you can't divide by 0)
            #and positive (for the output to make sense), if it is, the function will return or output it
            if num_of_people > 0:
                return num_of_people
            # if the
            else:
                print("Stop trying to break my code. It won't work.")
                continue
        except ValueError:
            print(
                "That input was not valid. How many people are splitting the bill? "
                )


def calculate_total():
    while True:
        # calling the functions above and setting their returns to variables
        sub_cost = cost_of_food()
        tip = add_tip() / 100
        bill_split = split_bill()
        # calculating the bill by muultiplying the cost of the food times the bill and then adding on the tax
        total_bill = (sub_cost * tip) + (sub_cost * 1.1)
        # calculating how much each person would pay and rounding the float to 2 digits, if the division is longer than that
        each_pays = (total_bill / bill_split)
        print(f"Your total bill including a 10% sales tax and tip is: ${total_bill:.2f}")
        print(f"Each person should pay: ${each_pays:.2f}")
        # requesting input from the user if they would like to start over or to end the program
        #The .upper() just ensures that if the user mistakenly types "y" it will also work to restart the program.
        to_do_next = input('Would you like to calculate another tip? If so, type "Y": ').upper()
        if to_do_next == "Y":
            continue
        else:
            break


calculate_total()
