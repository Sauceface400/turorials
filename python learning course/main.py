from random import randint

choises = ["rock","paper","scissors"]
def Main_game():
    computer = choises[randint(0,2)] #The randint is basically for the computer choosing a random number

    print("Welcome to the rock paper scissors game\n")
    player = input("Your choice: ").lower() #this line o code is so that you can write in the console
    print("computer choose: " + computer)

    if player == computer:
        print("DRAW!")
    elif player == "rock" and computer == "paper":
        print("player lose")
    elif player == "rock" and computer == "scissors":
        print("player wins")
    elif player == "paper" and computer == "scissors":
        print("player lose")
    elif player == "paper" and computer == "rock":
        print("player wins")
    elif player == "scissors" and computer == "rock":
        print("player lose")
    elif player == "scissors" and computer == "paper":
        print("player wins")
    
    Main_game()

Main_game()


