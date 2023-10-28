# What are the rules of writing variable names.

myFavColor = "White"

myFavColorDress = "Brown"

myFavColorCar = "Light Dark"

print(myFavColorCar)

# 12hello = "something"  ->> Not valid

# It works
name1233 = "hello"

#1 Rule:
# Keywords cannot be the name of the variables
# for = 45 (Not valid because for is a keyword)


#2 Rule: Identifiers can consist of small caps letters uppercase digits and underscores (_)
# myage = 56 (valid name of the variable)

#3 Rule: Identifiers cannot begin with numbers (digits)
# 1hello = "value" (NOt valid because it starts with a number)

#4 Rule: Cannot contain only digits 
# 2345345 = "value" ---- NOT valid

#5 Rule: It can start with an underscore (_)
# _mycar = "Toyota" -> VALID because start with _ and consist of letters only


#6 Rule: No limit on the lenght of identifier
#  a = 34 OR ajsdfkhdfjghsjdfhkglshldkfhglksjdhflkgjshdlfkjhgslikdfhgklshdfljkghsljdkfhgskldfhg = "value " (Both valid no limits)
# $hcaptcha_secret = "key"
# $response = 1

#7 Rule: The names are case sensitive.
#  ABC and abc are not equal and they are considered different.
# Abc != abc OR  xYz!= XYZ
# ABC is not equal to abc (Because the first is in capital case and the second is in small caps)

#8 Rule: We cannot use space between the variable names
# my name = "Adil" --- NOT valid name. Why because we have a space between my and name, There should be no space (myname OR myName OR my_name OR MyName OR MYNAME)

#9 Rule: We can write numbers in between the letters or at the end of the variable name.
# h1 = "Hiiii" (VALID, because the digit 1 is at the end)
my12name = 342342
print(my12name)

yeab = 12
Yeab = 45

# No qoutation marks needed, why?? Because we are defining these words so the code knows them.
print(Yeab)

# so if it is not a variable name we have to use the Quotation mark
print("Hello this is something that I want to say :D")


