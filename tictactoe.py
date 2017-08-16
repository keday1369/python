def print_board(board):
    row = 1
    number = 0
    while row < 4:
        print(" " + str(board[number]) + " | " + str(board[number + 1]) + " | " + str(board[number + 2]))
        if row != 3:
            print("---+---+---")
        number += 3
        row += 1


def update_board(board, letter, position):
    board[position] = letter
    print_board(board)


def check_horizontal(board, row):
    a = board[row * 3 + 0]
    b = board[row * 3 + 1]
    c = board[row * 3 + 2]
    if a == b and a == c:
        print(board[a] + " wins!")
        return True


def check_vertical(board, column):
    a = board[column + 0]
    b = board[column + 3]
    c = board[column + 6]
    if a == b and a == c:
        print(board[a] + " wins!")
        return True


def check_full(board):
    for check in range(0, 9):
        if board[check] != "x" and board[check] != "o":
            return False
    print("Tie! Restart and try again.")
    return True


def check_diagonal(board, startpos):
    a = startpos
    if a != 0:
        b = startpos + 2
        c = b + 2
    else:
        b = startpos + 4
        c = b + 4
    if board[a] == board[b] and board[b] == board[c]:
        print(board[a] + " wins!")
        return True


def should_stop(board):
    for row in range(0, 3):
        if check_horizontal(board, row):
            print("We have a winner!")
            return True
    for column in range(0, 3):
        if check_vertical(board, column):
            print("We have a winner!")
            return True
    if check_diagonal(board, 0):
        return True
    if check_diagonal(board, 2):
        return True
    if check_full(board):
        return True
    return False

board = list(range(0, 9))
print_board(board)
letter = "x"
while not should_stop(board):
    update = input("Position: ")
    if board[int(update)] != "x" and board[int(update)] != "o":
        update_board(board, letter, int(update))
        if letter == "x":
            letter = "o"
        else:
            letter = "x"
    else:
        print("Error: the chosen position is already a letter. Please try again.")