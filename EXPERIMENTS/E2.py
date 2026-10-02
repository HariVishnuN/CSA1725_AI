def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
            
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
            
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
            
    return True

def solve_nq(board, col, n):
    if col >= n:
        return True
        
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            
            if solve_nq(board, col + 1, n):
                return True
                
            board[i][col] = 0
            
    return False

n = int(input("Enter the number of Queens (enter 8 for 8-Queens): "))
board = [[0 for _ in range(n)] for _ in range(n)]

if solve_nq(board, 0, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
else:
    print("Solution does not exist")