def get_valid_values(board, row, col):
    """Return a list of valid numbers that can be placed at (row, col)"""
    possible = set(range(1, 10))

    for i in range(9):
        possible.discard(board[row][i])
        possible.discard(board[i][col])

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            possible.discard(board[r][c])

    return list(possible)


def select_mrv_variable(board):
    """Select the empty cell (row, col) with the fewest legal values (MRV heuristic)"""
    min_options = 10
    best_cell = None

    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                options = get_valid_values(board, r, c)
                if len(options) < min_options:
                    min_options = len(options)
                    best_cell = (r, c)
                if min_options == 1:
                    return best_cell
    return best_cell


def least_constraining_values(board, row, col):
    """Return values for the cell sorted by least-constraining order"""
    values = get_valid_values(board, row, col)

    def constraint_impact(val):
        count = 0
        board[row][col] = val
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    count += len(get_valid_values(board, r, c))
        board[row][col] = 0
        return count

    return sorted(values, key=constraint_impact, reverse=True)


def solve_sudoku(board):
    cell = select_mrv_variable(board)
    if not cell:
        return True  

    row, col = cell
    for num in least_constraining_values(board, row, col):
        board[row][col] = num
        if solve_sudoku(board):
            return True
        board[row][col] = 0
    return False


def print_board(board):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("-" * 21)
        for c in range(9):
            if c % 3 == 0 and c != 0:
                print("|", end=" ")
            print(board[r][c] if board[r][c] != 0 else ".", end=" ")
        print()