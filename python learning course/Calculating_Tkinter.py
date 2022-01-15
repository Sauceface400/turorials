Board = [
    "-","-","-",
    "-","-","-",
    "-","-","-"
]

game_is_not_over = True

winner = None

current_player = "X"

def diplay_board():
    print(Board[0] + "|" + Board[1] + "|" + Board[2])
    print(Board[3] + "|" + Board[4] + "|" + Board[5])
    print(Board[6] + "|" + Board[7] + "|" + Board[8])

def play_game():
    diplay_board()
    while game_is_not_over:
        handle_turn(current_player)
        
        check_if_the_gameover()

        swap_player()
    if winner == "X" or winner == "O":
        print(winner + "wins.")
    elif winner == None:
        print("Tie. ")

def handle_turn(player):
    print(player + "'s turn.")

    position = input("Enter your position from 1-9: ")  
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Invalid input, Enter your position from 1-9: ")

        position = int(position) - 1

        if Board[position] == "-":
            valid = True
        else:
            print("you cant place here enter another postion.")
    

    Board[position] = player

    diplay_board()

def check_if_the_gameover():
    check_if_win()
    check_if_tie()

def swap_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

def check_if_win():
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner()
    elif column_winner:
        winner = column_winner()
    elif diagonal_winner:
        winner = diagonal_winner()
    else:
        winner = None
    
    return

def check_rows():
    global game_is_not_over
    row1 = Board[0] == Board[1] == Board[2] !="-"
    row2 = Board[3] == Board[4] == Board[5] !="-"
    row3 = Board[6] == Board[7] == Board[8] !="-"

    if row1 or row2 or row3:
        game_is_not_over = False

    if row1:
        return Board[0]
    elif row2:
        return Board[3]
    elif row3:
        return Board[6]
    return

def check_columns():
    global game_is_not_over
    column1 = Board[0] == Board[3] == Board[6] !="-"
    column2 = Board[1] == Board[4] == Board[7] !="-"
    column3 = Board[2] == Board[5] == Board[8] !="-"

    if column1 or column2 or column3:
        game_is_not_over = False
    if row1:
        return Board[0]
    elif row2:
        return Board[1]
    elif row3:
        return Board[2]    
    return

def check_diagonal():
    global game_is_not_over
    diagonal1 = Board[0] == Board[4] == Board[8] !="-"
    diagonal2 = Board[2] == Board[4] == Board[6] !="-"
    
    if diagonal1 or diagonal2:
        game_is_not_over = False
    if diagonal1:
        return Board[0]
    elif diagonal2:
        return Board[2]
    return

def check_if_tie():
    if "-" not in Board:
        game_is_not_over = False
    return

play_game()

