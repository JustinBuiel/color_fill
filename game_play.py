def player(board, size):
    global board_size
    board_size = size
    user_choice = input("Enter color: ")
    global color_to_mark
    lst = []
    color_to_mark = board[0][0]
    check_all(board, (0,0), lst)
    for row in board:
        for i in range(len(row)):
            if row[i] == 'marked':
                row[i] = user_choice


def check_all(board, index: tuple, lst: list):
    row, col = index

    if row == 0 and col == 0:
        board[row][col] = 'marked'
    else:
        del lst[0]

    if row != 0:
        val = check_up(board, index)
        if val is not None:
            lst.append(val)
    if col != 0:
        val = check_left(board, index)
        if val is not None:
            lst.append(val)
    if col != board_size - 1:
        val = check_right(board, index)
        if val is not None:
            lst.append(val)
    if row != board_size - 1:
        val = check_down(board, index)
        if val is not None:
            lst.append(val)

    if lst:
        check_all(board, lst[0], lst)
    else:
        return


def check_up(board, index):
    if board[index[0]-1][index[1]] == color_to_mark:
        board[index[0]-1][index[1]] = 'marked'
        return (index[0]-1, index[1])
    else:
        return 


def check_left(board, index):
    if board[index[0]][index[1]-1] == color_to_mark:
        board[index[0]][index[1]-1] = 'marked'
        return (index[0], index[1]-1)
    else:
        return 


def check_right(board, index):
    if board[index[0]][index[1]+1] == color_to_mark:
        board[index[0]][index[1]+1] = 'marked'
        return (index[0], index[1]+1)
    else:
        return 


def check_down(board, index):
    if board[index[0]+1][index[1]] == color_to_mark:
        board[index[0]+1][index[1]] = 'marked'
        return (index[0]+1, index[1])
    else:
        return 