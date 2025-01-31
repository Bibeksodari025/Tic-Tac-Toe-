# Tic-Tac-Toe-
This Tic Tac Toe game in Python is a two-player terminal game. It’s split into four parts: game.py handles game logic, board.py displays the board and checks win conditions, player.py manages player input, and run_game.py starts the game. Players alternate placing X or O on a 3x3 grid.

This Tic Tac Toe game is a simple yet fun Python implementation, where two players take turns to place their symbols (X or O) on a 3x3 grid. The game logic is divided into four parts:

1. **Game Logic**: The core of the game is in the `game.py` file, where players alternate turns, and the game checks for a winner or draw after every move.

2. **Board Display**: The `board.py` file handles how the board is shown to players and checks if any player has won or if the game has ended in a draw.

3. **Player Interaction**: The `player.py` file ensures that players can only choose available spots on the board and enter valid numbers.

4. **Entry Point**: The `run_game.py` file is where the game starts, simply calling the function that starts the game.

This modular design keeps the code clean and organized, allowing each part of the game to focus on a specific task, such as managing the board or player input. The game continues until one player wins or the game is a draw, making it an easy and fun way to play Tic Tac Toe in the terminal.
