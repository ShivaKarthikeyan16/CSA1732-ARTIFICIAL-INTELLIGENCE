board = [' ' for _ in range(9)]

def print_board():
    print('|'.join(board[0:3]))
    print('-' * 5)
    print('|'.join(board[3:6]))
    print('-' * 5)
    print('|'.join(board[6:9]))

def player_move(icon):
    player = 1 if icon == 'X' else 2
    print("Player {}'s turn".format(player))

    choice = int(input("Enter your move (1-9): "))

    if 1 <= choice <= 9 and board[choice - 1] == ' ':
        board[choice - 1] = icon
    else:
        print("Invalid move!")
        player_move(icon)

def is_victory(icon):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    return any(all(board[i] == icon for i in line) for line in wins)

def is_draw():
    return ' ' not in board

while True:
    print_board()
    player_move('X')

    if is_victory('X'):
        print_board()
        print("X Wins! Congratulations!")
        break

    if is_draw():
        print("It's a Draw!")
        break

    print_board()
    player_move('O')

    if is_victory('O'):
        print_board()
        print("O Wins! Congratulations!")
        break

    if is_draw():
        print("It's a Draw!")
        break
