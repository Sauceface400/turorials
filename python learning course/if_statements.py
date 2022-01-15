male = True
mass = False

if male and mass:
    print("you are a male and overweight")
elif not(male) and mass:
    print("overweight and female")
elif male and not(mass):
    print("not an overweight male")
else: 
    print("you are a female and not overweight")

#=========================EXAMPLE'S==============================================
what_is_gender = input("Insert your gender here: ")
What_is_the_weight = int(input("put on mass here: "))

if what_is_gender == "female":
    print("your a feamle")
elif what_is_gender == "male":
    print("you are a male")
else:
    print("there is no third gender")

if What_is_the_weight > 40:
    print("you are over 40kg")
else:
    print("you are less than 40kg")
    