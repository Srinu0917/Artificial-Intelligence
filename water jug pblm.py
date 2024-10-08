def is_safe(board, row, col):
    # Check this column on the upper side
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper diagonal on the right side
    for i, j in zip(range(row, -1, -1), range(col, len(board), 1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, row):
    # If all queens are placed
    if row >= len(board):
        return True
    
    # Consider this row and try placing this queen in all columns one by one
    for col in range(len(board)):
        if is_safe(board, row, col):
            # Place this queen in board[row][col]
            board[row][col] = 1
            
            # Recur to place the rest of the queens
            if solve_n_queens_util(board, row + 1):
                return True
            
            # If placing queen in board[row][col] doesn't lead to a solution, then remove the queen
            board[row][col] = 0
    
    # If the queen cannot be placed in any column in this row, then return False
    return False

def solve_n_queens():
    board = [[0 for _ in range(8)] for _ in range(8)]
    
    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")
        return False
    
    print_board(board)
    return True

def print_board(board):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))

# Solve the 8-Queen problem
solve_n_queens()