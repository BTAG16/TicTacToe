def display_board(table):
    print(f"{table[0]} | {table[1]} | {table[2]}")
    print(f"---------")
    print(f"{table[3]} | {table[4]} | {table[5]}")
    print(f"---------")
    print(f"{table[6]} | {table[7]} | {table[8]}")

def player_input(table, player):
    while True:
        try:
            position = int(input(f"Player {player} Enter a position(1 - 9): ")) - 1
            if table[position] == " ":
                table[position] = player
                break
            else:
                print("This position has been occupied. Try again!")
        except (ValueError, IndexError):
            print("Invalid input. Choose a number between 1 and 9.")

def check_win(table, player):
    win_pos = [
        [0,3,6], [1,4,7], [2,5,8], [0,1,2], [3,4,5], [6,7,8], [0,4,8], [2,4,6]
    ]
    for positions in win_pos:
        if table[positions[0]] == table[positions[1]] == table[positions[2]] == player:
            return True
    return False

def check_tie(table):
    return " " not in table

def play_game():
    board = [" " for _ in range(9)]
    players = ['X', 'O']
    current_player = 0

    while True:
        display_board(board)
        player_input(board, players[current_player])

        if check_win(board, players[current_player]):
            display_board(board)
            print(f"Player {players[current_player]} wins!")
            break
        elif check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        current_player = 1 - current_player

board = [" " for _ in range(9)]
play_game()