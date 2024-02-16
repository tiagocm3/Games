def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("--" * 5)

def check_winner(board, player):
    # Check rows, columns and diagonals for a win
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
                all([board[j][i] == player for j in range(3)]):
            return True

    if board[0][0] == board[1][1] == board[2][2] == player or \
            board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    for _ in range(9):
        print_board(board)
        row, col = map(int, input(f"Player {current_player}, enter row and column (0 2): ").split())
        if board[row][col] != " ":
            print("Invalid move, try again.")
            continue

        board[row][col] = current_player
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("It's a tie!")

tic_tac_toe()
