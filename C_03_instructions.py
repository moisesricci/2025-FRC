# functions go here
def make_statement(statement, decoration):
    """Emphasis headings by adding decoration at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


# Main Routine goes here
def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    while True:
        response = input(question).lower()

        for item in valid_answers:

            if response == item:
                return item

            elif response == item[:num_letters]:
                return item

        print(f"Please choose either {valid_answers}")


def instructions():
    print()
    make_statement(statement="Instructions", decoration="ℹ")
    print('''
This Program will ask you for...
    - The name of the product you are selling
    - How many items you plan on selling
    - The costs for each component of the product
        (Variable Expenses)
    - Whether or not you have fixed expenses ( if you have fixed expenses, it will ask you what they are).
    - How Much money you want to make (ie: your profit goal)
    
It will also ask you how much the recommended sales price should be rounded to
 
The program outputs an itemised list of the variable and fixed expenses (which
includes the subtotals for these expenses).

Finally it will tell you how much you should sell each item for to reach your profit goal

The data will also be written to a text file which has the name of your product and today's date.
     ''')


# Main routine goes here

make_statement(statement="Fundraiser Calculator", decoration="💰")

print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()
print("The program continues... ")
