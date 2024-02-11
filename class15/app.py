#  ctrl + j to open terminal

# to bring terminal up as a tab right click your mouse / touch pad to  and drag and drop the terminal in the tab area.

# to split screen in two section right click on the tab and split to the right side.

# list
my_items = [45, 56, 78, 89]

# syntax
# identifier = (items of tuple...)

# tuple - by Yeabsira
my_stuf = (42, False, 23, 78, "alex")

# definition of a tuple
billion = (401, 2, 4023, 1024, False, 4.5)

print(billion)

# valid
mil = ()

# single element tuple
mil_1 = (67)

# Acessing by index number
print(billion[2]) 

# first index is inclusive, the second excluded
print(billion[1:3]) 

# immutable nature we cannot modify a tuple
# billion[2] = 89 -> it will raise an error

# looping over a tuple -> do as a homework

i_am_packed = 45,56,67,78  #-> packing 

a, b, c,d = i_am_packed # unpacking

print(d)













