# pass
if 1> 3:
    pass

# break
# a keyword that can break the loop (stop the loop) based on a certain condition

greetings = "Happy holidays"
for greet in greetings:
    if greet == " ":
        break
    # print(greet)

# continue
# this statement can skip the iteration based on a certain condition
    
greetingss = "Happy holidays"
for greet in greetings:
    if greet == " ":
        continue
    # print(greet)


# string -> a sequence of characters enclosed in double qoutes / single/ triple

string_1 = ' I am single'
string_2 = "I am double "
print(string_2)
string_3 = ''' I am triple 
and I can

be in 
multiple lines '''


# print(string_3)

# methods -> piece of code that can do a certain functionality without us doing it. these methods can be called built-in functions in python.
# syntax
# len method
# print ( len("Hello there I am a string") )

# count method
my_message = "Hey I will learn to code in the next six months. All these months I am going to practice every day for all these months"
print("The count of months is: ", my_message.count("months"))

# format method
name_of_person = "alex"
age = 56

formated_string = "the person name is {} and his age is {}.".format(name_of_person, age)
print(formated_string)

# immutable -> not changable 
# strings are immutable
example = "Hello string"

# reintialize to change the value (mutable)
example = "helloo string"
# mutable -> something that can be changed
print(example)

# index -> position of string or an item in an array (list)
example2 = "oohoooo this is cool"
# substring (a sub-sequence of characters in a string)
example3 = example2[2:]
print(example3)


# boolean expression: It evaluates to either true or false.
# in operator
print ("h" in "hello")

# not in operator
print ("hsdhfj" not in "hello")
