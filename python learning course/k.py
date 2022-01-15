from random import randint

Moves = ["female","male"]

def gameOfChoice():
    FemPlayer = Moves[randint(0,1)]
    print("begin sexies")
    Maleplayer = input("Pick genders: ")
    print("female player pick:" + FemPlayer)

    if FemPlayer == Maleplayer:
        print("sexist")
    elif Maleplayer == "male" and FemPlayer == "female":
        print("racist bitch")
    elif Maleplayer == "female" and FemPlayer == "male":
        print("cunt head")
    else:
        print("NO THIRD GENDER MOTERFUCKING CUNT AND TWAT!")
    gameOfChoice()
gameOfChoice()