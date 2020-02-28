import sys

po = [[" ", " ", " "],
      [" ", " ", " "],
      [" ", " ", " "]]


def create_board(board):
    print("\n")
    print(board[0][0] + "  | " + board[0][1] + " | " + board[0][2])
    print(" - " + "+" + " - " + "+" + " - ")
    print(board[1][0] + "  | " + board[1][1] + " | " + board[1][2])
    print(" - " + "+" + " - " + "+" + " - ")
    print(board[2][0] + "  | " + board[2][1] + " | " + board[2][2])
    print("\n")


def check_current_state(board):
    winner = None
    for x in range(len(board[0])):                              # Checks all the columns
        if board[x][0] == board[x][1] == board[x][2]:
            winner = board[x][0]

    for i in range(len(board[0])):                              # Checks all the rows
        if board[0][i] == board[1][i] == board[2][i]:
            winner = board[0][i]

    if board[0][0] == board[1][1] == board[2][2]:               # Checks the top-left to bottom right diagonal
        winner = board[0][0]

    if board[0][2] == board[x][1] == board[2][0]:               # Checks the top-right to bottom-left diagonal
        winner = board[2][0]

    return winner


moves_list = {1: [0, 0], 2: [0, 1], 3: [0, 2],
              4: [1, 0], 5: [1, 1], 6: [1, 2],
              7: [2, 0], 8: [2, 1], 9: [2, 2]}


def player1_move(board):
    print("\n")
    print("PLAYER 1 TURN")
    print("\n")
    create_board(board)
    player_place = int(input("Where do you want to put the marker?: "))
    row, col = moves_list[player_place]

    if board[row][col] != " ":
        print("Space already occupied!")
        player1_move(board)
    else:
        board[row][col] = "X"

    if check_current_state(board) == "X":
        print("\n")
        print("PLAYER 1 WINS!!!")
        create_board(board)
        sys.exit()


def player2_move(board):
    print("\n")
    print("PLAYER 2 TURN")
    print("\n")
    create_board(board)
    player_place = int(input("Where do you want to put the marker?: "))
    row, col = moves_list[player_place]

    if board[row][col] != " ":
        print("Space already occupied!")
        player1_move(board)
    else:
        board[row][col] = "O"

    if check_current_state(board) == "O":
        print("\n")
        print("PLAYER 2 WINS!!!")
        create_board(board)
        sys.exit()


while " " not in po:
    player1_move(po)
    player2_move(po)


