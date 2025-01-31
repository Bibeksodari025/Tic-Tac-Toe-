from board import display_board, check_win, check_draw
from player import get_player_move

def start_game():
    board = [' ' for _ in range(9)]  # Board with 9 spaces (empty)
    current_player = 'X'
    game_over = False

    while not game_over:
        display_board(board)
        move = get_player_move(current_player, board)
        board[move] = current_player
        
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'

