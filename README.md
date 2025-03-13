# TicTacToe

This is a simple TicTacToe game implemented in Python. The game allows two players to take turns and play TicTacToe in the terminal.

## How to Run

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/TicTacToe.git
   ```

2. Navigate to the project folder:

   ```bash
   cd TicTacToe
   ```

3. Run the game by executing the `main.py` file:

   ```bash
   python main.py
   ```

4. The game will prompt each player to enter a position (1-9) to place their marker ('X' or 'O'). The board will update after each move.

## Features

- Two players take turns to place their marker on the board.
- The board is displayed after each move.
- The game checks for a win or a tie after every turn.
- The game ends when a player wins or if it's a tie.

## Functions

### `display_board(table)`
- Displays the current TicTacToe board.

### `player_input(table, player)`
- Prompts the player to choose a valid position (1 - 9) and places their marker on the board.

### `check_win(table, player)`
- Checks if the current player has won the game.

### `check_tie(table)`
- Checks if the game has ended in a tie (i.e., the board is full without any winner).

### `play_game()`
- Main function that starts the game, alternates players, and checks for a winner or tie.

## Example

```bash
Player X Enter a position(1 - 9): 1
X |   |  
---------
  |   |  
---------
  |   |  
```

After each turn, the board will be updated and shown in the terminal.

## License

This project is open-source and available under the MIT License.
