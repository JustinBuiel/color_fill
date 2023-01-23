import random


def create_board(size):
    colors = ['white', 'black', 'blue', 'red', 'yellow', 'orange']

    rows, cols = (size, size)
    board = [[0 for i in range(cols)] for j in range(rows)]

    for row in board:
        for col in range(len(row)):
            choice = random.randint(0, 60)

            if choice < 10:
                color = colors[0]
            elif choice < 20:
                color = colors[1]
            elif choice < 30:
                color = colors[2]
            elif choice < 40:
                color = colors[3]
            elif choice < 50:
                color = colors[4]
            else:
                color = colors[5]

            row[col] = color

    return board


def check_finish(board):
    curr_color = board[0][0]
    for row in board:
        for i in range(len(row)):
            if row[i] != curr_color:
                return False
    return True
