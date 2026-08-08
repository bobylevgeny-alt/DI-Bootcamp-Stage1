# board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# board_size = 3
# name_game = "TIC TAC TOE"

# def display_board():
#     print("*" * 17)

#     for i in range(3):
#         print(
#             f"*   {board[i * 3]} | "
#             f"{board[1 + i * 3]} | "
#             f"{board[2 + i * 3]}   *"
#         )

#         if i == 2:
#             break

#         print("*  ---|---|---  *")

#     print("*" * 17)

# def player_input(player):
#     while True:
#         position = input(
#             f"Игрок {player}, выберите клетку от 1 до 9: ")

#         if not position.isdigit():
#             print("Введите число.")
#             continue

#         position = int(position)

#         if position < 1 or position > 9:
#             print("Введите число от 1 до 9.")
#             continue

#         index = position - 1

#         if board[index] == "X" or board[index] == "O":
#             print("Эта клетка уже занята.")
#             continue

#         board[index] = player
#         break

# def check_draw(board):
#     for cell in board:
#         if cell != "X" and cell != "O":
#             return False

#     return True

# def check_win(board, player):
#     winning_combinations = [

#         [0, 1, 2],
#         [3, 4, 5],
#         [6, 7, 8],

#         [0, 3, 6],
#         [1, 4, 7],
#         [2, 5, 8],

#         [0, 4, 8],
#         [2, 4, 6]
#     ]

#     for combination in winning_combinations:
#         first = combination[0]
#         second = combination[1]
#         third = combination[2]

#         if (
#             board[first] == player
#             and board[second] == player
#             and board[third] == player
#         ):
#             return True

#     return False

# def play():
#     current_player = "X"

#     while True:
#         display_board()

#         player_input(current_player)

#         if check_draw(board):
#             display_board()
#             print("Все клетки заполнены!")
#             print("Игра окончена.")
#             break

#         if current_player == "X":
#             current_player = "O"
#         else:
#             current_player = "X"


# print(name_game)
# play()