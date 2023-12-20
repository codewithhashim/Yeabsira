# Loop
# for and while loop
# Iteration: A single repetition of a loop. We often talk about loops in terms of the number of iterations that it has.
# Iterator Variable: The variable that stores a value which will determine the number of iterations.


names = "Hello there!"
for name in names:
    print("The letter is: ", name)

if 2 > 5:
    pass

# Infinite Loop: A loop that will repeat forever, usually due to the
# iterator variable not being incremented.

# while loop: runs the code until a certain condition is true

# initiate the init variable to 1 to simply skip 0 instead of writing if statement.
init = 0
while init < 6:
    if init == 0:
        pass
    elif init != 0:
        print(init)
    init = init + 1

# Accumulator Variable: A variable defined outside of a loop that accumulates a value during the loop. 
num = 9 
while num < 12:
    print(num)
    num = num + 1

# infinite loop
while 1 > 0:
    pass