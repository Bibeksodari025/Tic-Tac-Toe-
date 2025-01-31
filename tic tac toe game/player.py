def get_player_move(player, board):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid input! Please enter a number between 1 and 9.")
            elif board[move] != ' ':
                print("This space is already taken. Choose another space.")
            else:
                return move
        except ValueError:
            print("Invalid input! Please enter a valid number between 1 and 9.")
