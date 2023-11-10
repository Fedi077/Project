def place_L_pieces(board, defect_x, defect_y, size, x, y):
    if size == 2:
        for i in range(x, x + size):
            for j in range(y, y + size):
                if i != defect_x or j != defect_y:
                    board[i][j] = 'L'
        return

    sub_size = size // 2
    mid_x, mid_y = x + sub_size, y + sub_size

    if defect_x < mid_x and defect_y < mid_y:
        place_L_pieces(board, defect_x, defect_y, sub_size, x, y)
    else:
        board[mid_x - 1][mid_y - 1] = 'L'
        place_L_pieces(board, mid_x - 1, mid_y - 1, sub_size, x, y)

    if defect_x < mid_x and defect_y >= mid_y:
        place_L_pieces(board, defect_x, defect_y, sub_size, x, mid_y)
    else:
        board[mid_x - 1][mid_y] = 'L'
        place_L_pieces(board, mid_x - 1, mid_y, sub_size, x, mid_y)

    if defect_x >= mid_x and defect_y < mid_y:
        place_L_pieces(board, defect_x, defect_y, sub_size, mid_x, y)
    else:
        board[mid_x][mid_y - 1] = 'L'
        place_L_pieces(board, mid_x, mid_y - 1, sub_size, mid_x, y)

    if defect_x >= mid_x and defect_y >= mid_y:
        place_L_pieces(board, defect_x, defect_y, sub_size, mid_x, mid_y)
    else:
        board[mid_x][mid_y] = 'L'
        place_L_pieces(board, mid_x, mid_y, sub_size, mid_x, mid_y)

def print_board(board):
    for row in board:
        print(' '.join(row))

n = 8
defect_x, defect_y = 7, 4
board = [['.' for _ in range(n)] for _ in range(n)]
place_L_pieces(board, defect_x, defect_y, n, 0, 0)
print_board(board)







