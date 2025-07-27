def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_draw(board):
    for row in board:
        for cell in row:
            if cell not in ["X", "O"]:
                return False
    return True

def play_game():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]
    
    current_player = "X"

    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (1-9): ")

        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("❌ Invalid input. Try a number between 1 and 9.")
            continue

        move = int(move)
        row = (move - 1) // 3
        col = (move - 1) % 3

        if board[row][col] in ["X", "O"]:
            print("❌ That spot is taken. Try another.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("😐 It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()
