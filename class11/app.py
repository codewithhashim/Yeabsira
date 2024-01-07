# in and not in operator
# print("h" in "hellooo")
# print("h" not in "hellooo")

# range() function provides us a sequence of numbers(integer) where we can give it two parameters (the start value is optional) where the start value is inclusive and the stop value is exclusive.


# using break statement to exit out of loop.
# break
for i in range(5):
    if i==3:
        break
    print(i)

# continue statement help us skip the current iteration. This means if we write an if statement on a certain number or a certain condition and we want to skip that number or that value we can use the continue statement to skip that iteration.

# continue
for ij in range(10, 19):
    if ij == 15:
        continue
    # print(ij)

# list -> A data type where we can store values of different types under one identifier name. It is mutable data type.

# where do we start the index from?
# we start the index from 0.

# 0, 1,2,3,4,5,6,7,8,9,10,11.......

# list items are the elements that we write in a list by separating it using a comma (,)

# square brackets []. The list items are enclosed in square brackets.
my_items = ["hello", 56, 67, "alex", True, [12, 45, 56], ["alex"]]

# accessing a value
print(my_items[5][2])
# modifying an array
my_items[1] = 99
# print(my_items)


# array of students
# we can write arrays inside of one array
students = [
    ["alex", "david", "eli", "ali"],
    [12, 45, 10, 2],
    ["a", "c", "f", "b"]
]
print(students[2][3])