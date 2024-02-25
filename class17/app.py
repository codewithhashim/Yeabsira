# functions

# a block of organized, reusable code that is used to perform a single, related action.

# syntax

def function_name():
    # function body
    # print("I will do whatevr you ask! ")
    pass


# function call / function invocation
function_name()


# A practical use case:

def askTeacher():
    question = input("Can we take an off tomorrow? ")
    print("The teacher says: ", question)
    confirm_from_principal()


def confirm_from_principal():
    print("The principal always say YES!")


def holiday():
    print("Is tomorrow a holiday? ")
    askTeacher()


# call the holiday function to run the logic above.
# holiday()


# Parameters -> user_order
def my_resturant(user_order):
    print("Your ordered ", user_order, " and enjoy it!")


user_order = input("What would you like? ")
# argument -> user_order
my_resturant(user_order)

# print is a function call to another function
# print("hasdhfaksdjhf")
