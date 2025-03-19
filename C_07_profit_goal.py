# functions go here...
def yes_no_check(question):
    """Checks that users enter yes / y or no / n """

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no (y / n).\n")


def profit_goal(total_costs):
    error = "Please enter a valid profit goal\n"
    profit_type = ""
    amount = 0

    valid = False
    while not valid:

        response = input("What is your profit goal (eg $500 or 50%): ")

        if response[0] == "$":
            profit_type = "$"
            amount = response[1:]

        elif response[-1] == "%":
            profit_type = "%"
            amount = response[:-1]

        else:
            profit_type = "unknown"
            amount = response

        try:
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no_check(f"Do you mean ${amount:.2f}. ie {amount:.2f} dollars? ")

            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no_check(f"Do you mean {amount}%? ")
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
        return goal


while True:
    total_expenses = 200
    target = profit_goal(total_expenses)
    sales_target = total_expenses + target
    print(f"Profit Goal: ${target:.2f}")
    print(f"Sales Target: ${sales_target:.2f}")
    print()
