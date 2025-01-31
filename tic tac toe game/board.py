def display_board(board):
    # Print the board in a 3x3 grid format
    print("\n")
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")
    print("\n")

def check_win(board, player):
    # Check if the player has won the game
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]              # diagonal
    ]
    
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False

def check_draw(board):
    # Check if the board is full and there is no winner
    return ' ' not in board
