def get_char(value):
    if value<10:
        return chr(value+ord('0'))
    else:
        return chr(value-10+ord('A'))

def in_column(board, c, column):
    for row in range(16):
        if board[row][column] == c:
            return True
    return False

def in_quadrant(board, c, row,column):
    quadrant_row = int(row/4)*4
    quadrant_col = int(column/4)*4

    for i in range(4):
        for j in range(4):
            if board[quadrant_row+i][quadrant_col+j] == c:
                return True
    return False



def fill_blanks(board):
    count = 0
    for i in range(16):
        for j in range(16):
            if board[i][j] == '-':
                for try_value in range(16):
                    c = get_char(try_value)
                    if (c in board[i]) or in_column(board, c,j) or in_quadrant(board, c, i, j):
                        continue
                    else:
                        board[i][j] = c
                        count += 1
                        break
    return count


def input_row():
    row = []
    line = input()
    for c in line:
        row.append(c)
    return row


def do_case():
    board = []
    for i in range(16):
        row = input_row()
        board.append(row)
    num_filled = fill_blanks(board)
    print(num_filled)


for i in range(3):
    do_case()
