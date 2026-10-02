def solve_8_puzzle(start, goal):
    queue = [[start, [], [start]]]
    visited = set()
    while len(queue) > 0:
        current = queue.pop(0)
        board = current[0]
        moves = current[1]
        board_history = current[2]
        if board == goal:
            print("\n=== SOLUTION FOUND ===")
            print(f"Total Steps: {len(moves)}\n")
            for i in range(len(board_history)):
                if i == 0:
                    print("Start State:")
                else:
                    print(f"Move {i}: {moves[i-1]}")                
                b = board_history[i]
                print(f"{b[0]} {b[1]} {b[2]}")
                print(f"{b[3]} {b[4]} {b[5]}")
                print(f"{b[6]} {b[7]} {b[8]}")
                print("-" * 10)
            return
        board_tuple = tuple(board)
        if board_tuple in visited:
            continue
        visited.add(board_tuple)
        zero = 0
        for i in range(9):
            if board[i] == 0:
                zero = i
                break
        valid_moves = []
        if zero % 3 > 0: valid_moves.append([zero - 1, "Left"])
        if zero % 3 < 2: valid_moves.append([zero + 1, "Right"])
        if zero // 3 > 0: valid_moves.append([zero - 3, "Up"])
        if zero // 3 < 2: valid_moves.append([zero + 3, "Down"])
        for m in valid_moves:
            target = m[0]
            direction = m[1]
            new_board = []
            for num in board:
                new_board.append(num)
            new_board[zero] = new_board[target]
            new_board[target] = 0
            if tuple(new_board) not in visited:
                new_moves = list(moves)
                new_moves.append(direction)
                new_history = list(board_history)
                new_history.append(new_board)
                queue.append([new_board, new_moves, new_history])
    print("No solution found for this input.")
def get_user_board():
    board = []
    print("(Use 0 for the blank space)")
    for i in range(3):
        user_input = input(f"Enter 3 numbers for Row {i+1} separated by spaces: ")
        for num in user_input.split():
            board.append(int(num))
    return board
print("--- Enter the START state ---")
start_board = get_user_board()
print("\n--- Enter the GOAL state ---")
goal_board = get_user_board()
print("\nSearching for the shortest path... (Please wait)")
solve_8_puzzle(start_board, goal_board)