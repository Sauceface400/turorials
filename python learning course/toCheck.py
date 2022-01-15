def evenNum(num):
     return num % 2 == 0 #this the shortcut if you donot want to use if/else statement
def evenNum(numbers):
    if numbers % 2 == 0:#the % is use for divisable(boleh dibahagikan)
        return True
    else:
        return False

def test ():
    assert evenNum (2) == True
    assert evenNum (4) == True
    assert evenNum (6) == True
    assert evenNum (7) == False
    print("coding is correct")
test()

j = "kaki aku sakit" #len is use to count how many alphabets are there in a string or words
print(len(j))

def LengthOfWords(Length): #this is to check wether you number of alphabets are correct
    return (len(Length))
    

def testingTheString():
    assert LengthOfWords ("kill") == 4
    print("You've done it baby, WOOOW!")
testingTheString()

def LastWords(theLast): #this is for showing the last aplhabet
    return (theLast[-1])

def testing():
    assert LastWords("jack likes you hahaha") == "a"
    print("binggo baby")
testing()

def Big_num (B1,B2): #This is to find the bigger value of the two numbers
    if B1 > B2:
        return B1
    else:
        return B2

def test ():
    assert Big_num(1,2) == 2
    assert Big_num(100,358) == 358
    print("betul")
test()

def Big_num (B1,B2,B3): #This is to find the bigger value of the three numbers
    if B1 > B2:
        return B1
    elif B2 > B1 and B2 > B3:
        return B2
    else:
        return B3
def test ():
    assert Big_num(1,2,8) == 8
    assert Big_num(100,358,1000) == 1000
    print("betul")
test()

def BiggestNum (n1,n2,n3):
    return max(n1,n2,n3)

def test ():
    assert BiggestNum(2,6,10) == 10 #this is the short cut for finding the highest of the three numbers
    print ("betul")

def The_winner (winner):
    if winner == "Farhan":
        return 1
    elif winner == "John":
        return 2
    else:
        return 3

def The_winnerS_name(name):
    if name == 1:
        return "Farhan"
    elif name == 2:
        return "John"
    else:
        return "ellizabeth"

def The_winner (winner):
    return {"Farhan": 1,"John" : 2,"ellizabeth" : 3}[winner]
    


def The_winnerS_name(name):
    return {1 : "Farhan",2 : "John",3 : "ellizabeth"}[name]


def test2():
    assert The_winner("Farhan") == 1
    assert The_winner("John") == 2
    assert The_winner("ellizabeth") == 3 

def test1():
    assert The_winnerS_name(1) == "Farhan"
    assert The_winnerS_name(2) == "John"
    assert The_winnerS_name(3) == "ellizabeth"

test1()
test2()
print("Jack is right")





