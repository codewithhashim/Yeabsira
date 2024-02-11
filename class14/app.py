
# index numbers
# 0,1,2,3,4,5,6,7,8,9,10.....
my_list = [45, "hello", "store", True, 12.2, 45]
# print(my_list[3])

# an element in a list is some data that we separate it with a (,)

number_count = my_list.count(45)
# print(number_count)

# Example by Yeabsira
my_info = [12, "alex", 42, False, 12]
# print(my_info[2])

info_count = my_info.count(12)
# print(info_count)


random_numbers = [45, 12, 3, 4, 5, 6, 4345,
                  2, 34, 53, 23, 454, 24, 24, 234, 234]
# random_numbers.sort(reverse=True)
# print(random_numbers)

random_numbers.reverse()
# print(random_numbers)


names_of_students = ["ed", "ben", "hailey", "sasha"]
# print(len(names_of_students))
# incrementing variable / value
count = 0 
while (count < len(names_of_students)):
    print(names_of_students[count])
    count = count + 1

