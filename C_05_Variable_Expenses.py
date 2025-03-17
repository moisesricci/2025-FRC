import pandas

# Functions go here
def num_check(question, num_type="float", exit_code = None):
    """Checks users enter an integer / float that is more than zero (or the optional exit code)"""

    if num_type == "float":
        error = "Please enter a number more than zero."
    else:
        error = "Please enter an integer more than zero."

    while True:

        response = input(question)

        if response == exit_code:
            return response

        try:

            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank.")


def get_expenses(exp_type, how_many):
    """Gets variable / fixed expenses and outputs panda (as a string) and a subtotal of the expenses"""

    # lists for panda
    all_items = []
    all_amounts = []
    all_dollar_per_item = []

    # expenses dictionary
    expenses_dict = {
        "Item": all_items,
        "Amount": all_amounts,
        "$ / Item": all_dollar_per_item
    }
    amount = 1

    # loop to get expenses
    while True:
        item_name = not_blank("Item name:")

        # check users enter at least one variable expense
        if (exp_type == "variable" and
            item_name == "xxx") and len(all_items) == 0:
            print("Oops - you have not entered anything. "
                  "You need at least one item")
            continue

        elif item_name == "xxx":
            break

        amount = num_check(f"How many <enter for {how_many}>: ", num_type = "integer", exit_code ="")

        if amount == "":
            amount = how_many

        cost = num_check(question="Price for one? ", num_type = "float")

        all_items.append(item_name)
        all_amounts.append(amount)
        all_dollar_per_item.append(cost)

    expense_frame = pandas.DataFrame(expenses_dict)

    expense_frame['Cost'] = expense_frame['Amount'] * expense_frame['$ / Item']

    subtotal = expense_frame['Cost'].sum()


    return expense_frame, subtotal

    # return all items for now, so we can check loop.
    return all_items

# Main routine starts here

quantity_made = num_check(question="Quantity being made: ",
                          num_type="integer")
print()

print("Getting Variable Costs...")
variable_expenses = get_expenses(exp_type="variable", how_many=quantity_made)
print()
variable_panda = variable_expenses[0]
variable_subtotal = variable_expenses[1]

print(variable_panda)
print(variable_subtotal)

