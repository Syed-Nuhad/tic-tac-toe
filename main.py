def print_board(board):
    print()
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print()


def check_winner(board, player):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in wins)


def is_draw(board):
    return all(cell in ['X', 'O'] for cell in board)


def tic_tac_toe():
    board = [str(i + 1) for i in range(9)]  # board = ['1','2',...,'9']
    current_player = 'X'

    print("Welcome to Tic Tac Toe!")
    print("Enter a number (1-9) to place your mark:")

    while True:
        print_board(board)
        move = input(f"Player {current_player}, choose your move (1-9): ")

        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("❌ Invalid input. Enter a number from 1 to 9.")
            continue

        idx = int(move) - 1
        if board[idx] in ['X', 'O']:
            print("❌ That spot is already taken. Try another one.")
            continue

        board[idx] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
tic_tac_toe()

