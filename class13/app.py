if 2 > 11:
    print()
    # 2 is less so it is not gonna work
    print("Hello yes it is less than 2")

    # this for loop is in the block of the if statement above.

    # intentionally produced semantic error.
    for i in range(5):
        print(i)
        for i in range(10):
            print()
            for li in range(14):
                print()


print("Hi, independent")

# syntax (English)
# I am eating an apple. -> syntax is correct.

# an apple is eating me. -> syntax is correct, but it does not make any sense.

# semantic error (logical error)(defined in doc)


# list (previously well-explained) - a built-in data type
# collection of items
mylist = [5, "hello", 12, "hi", True]

# methods: built-in functions that are supposed to do something.


mylist.append("in the movie part 4")
print(mylist)

mylist.remove(12)
mylist.remove("in the movie part 4")
print(mylist)

mylist.pop()
