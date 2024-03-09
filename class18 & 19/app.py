sets_of_data = (56, 67, 89)

# function
# A block of organized, reusable code that is used to perfom a single/multiple, related action/s.
#
#

# syntax:


def notification():
    # print("here is a notification, tiongggg!")
    pass


# function call (function invocation) invoking a function
notification()


def eat_pizza():
    pass
    # print("eat it ")


eat_pizza()


def soccer_time():
    # print("score a goal")
    pass


soccer_time()

# def is a keyword that defines a function

# break_time is an identrifier that denotes a function name

#  the parenthesis () represents the usage of a function.


def break_time():
    # this is a function body
    # print("take a break from soccer")
    pass


# this is a function call.
break_time()


def python_time():
    # print("time to code")
    pass


python_time()


def say_hello():
    pass


# print(say_hello())
# say_hello()

# parameters -> parameters is the  information that we pass to the function.

# when we pass the data in function definition we call it parameters.
def add(a, b):
    return a / b

# arguments -> when we pass it to the function call we call it arguments.
# print(add(12, 2))


# scope
def call_adam():
    call = "calling..."
    print("ok good", call)


call_adam()
# if we try to access a local scoped variable we will get a NameError.
# print("ok good", call)

# scope
# local scope
# IF A  VARIABLE IS DEFINED INSIDE A FUNCTION, THAT IS A LOCAL SCOPE.
# global scope
# WHEN A VARIABLE IS DEFINED IN A PLACE WHERE WE CAN ACCESS THAT VARIABLE FROM ANYWHERE IN THE CODE.


# globally scoped variable
call_anwar = "Hello anwar!"
print(call_anwar)


def calling():
    print(call_anwar)


calling()

# default parameter

# you cannot write any parameter after the default parameter.

# if the number of arguments do not match wit the number of parameter we will get an error.


# def type(abc, jelly="yes jelly is sweet.", asd):
#     print(jelly)
#     print(abc)


# # default argument
# type(abc="xyz", asd=45)


# default parameter
def hello_hi(hi, hello=67):
    print(hello)
    print(hi)


# default argument
hello_hi(hi=567)
