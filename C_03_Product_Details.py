# Functions go here
def num_check(question, num_type="float"):
    """Checks users enter an integer / float that is more than zero (or the optional exit code)"""

    if num_type == "float":
        error = "Please enter a number more than zero."
    else:
        error = "Please enter an integer more than zero."

    while True:

        try:

            if num_type == "float":
                response = float(input(question))
            else:
                response = int(input(question))

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


while True:

    product_name = not_blank("Product Name:")
    quantity_name = num_check(question="Quantity being made:", num_type="integer")
    print(f"You are making {quantity_name} {product_name}")
    print()
