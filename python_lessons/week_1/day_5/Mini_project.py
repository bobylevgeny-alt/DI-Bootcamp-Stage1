board = [1,2,3,4,5,6,7,8,9]
board_size = 3
name_game=('TIC TAC TOE')
def display_board():
    print("*" * 17)
    for i in range(3):
        
        print(f"*   {board[i*3]} | {board[1+i*3]} | {board[2+i*3]}   *")
        if i == 2:
            break
        print("*"+"  "+"---"+"|"+"---"+"|"+"---"+"  "+"*")
    print("*" * 17)        
    
print(name_game)
display_board()

def player_input(player):
    while True:
        try:
            position = int(input(f"Player {player}, choose from 1 to 9:"))
            if position < 1 or position > 9:
                print("Putt number from 1 to 9:")
                continue

            index = position - 1
            if board[index] == "X" or board[index] == "O":
                print("Error")
                continue

            board[index] = player
            break

        except ValueError:
            print("Putt a number.")

player_input("X")

display_board()

# def player_input(player):
#     pass

# def check_win(board, player):
#     display_board

# def check_draw(board, player):
#     display_board

# def play():
#     pass

