# pass
if 1> 3:
    pass

# break
# a keyword that can break the loop (stop the loop) based on a certain condition

greetings = "Happy holidays"
for greet in greetings:
    if greet == " ":
        break
    print(greet)

# continue
# this statement can skip the iteration based on a certain condition
    
greetingss = "Happy holidays"
for greet in greetings:
    if greet == " ":
        continue
    print(greet)