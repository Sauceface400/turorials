from math import *

for nombor in range(20,51):
    print(nombor)

count = 0
for addingCount in range(1,4):
    count = count + addingCount #This line means the old count will + to the addingCount or (0+1+2+3)
print(count)

def adding_Num(adding_Num):
    count = 0
    for addingCount in adding_Num:
        count = count + addingCount
    return count

assert adding_Num ([1,2,3]) == 6  #the assert is to test your code if your
                                  #code is wrong then it'll print out assert error if its right it wont print anything
print(adding_Num([1,2]))

def Making_sqaue_num(SquareNum):
    return SquareNum ** 2

assert Making_sqaue_num (2) == 4
print("coding is correct")

print(ceil(8.9 + 6.8))

name = input("State your name: ")
age = input("State your age as well: ")

print("Hello sir " + name + " welcome to our facility and please enter your age to varify. Thank you, your age is " + age)

colour = input("Enter colour: ")
nouns = input("Enter nouns: ")
celeberty = input("Enter celeberty: ")

print("I love the colour " + colour)
print(nouns + " are the best kind of thing")
print("I also love " + celeberty)
