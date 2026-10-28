def evaluate(state):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if state[a] == state[b] == state[c] == 'X':
            return 1
        if state[a] == state[b] == state[c] == 'O':
            return -1

    return 0

def game_over(state):
    return evaluate(state) != 0 or ' ' not in state

def get_possible_moves(state):
    return [i for i in range(9) if state[i] == ' ']

def make_move(state, move, player):
    new_state = state[:]
    new_state[move] = player
    return new_state

def minimax(state, depth, player):
    if depth == 0 or game_over(state):
        return evaluate(state)

    if player == 'X':
        best_score = float('-inf')

        for move in get_possible_moves(state):
            new_state = make_move(state, move, player)
            score = minimax(new_state, depth - 1, 'O')
            best_score = max(best_score, score)

        return best_score

    else:
        best_score = float('inf')

        for move in get_possible_moves(state):
            new_state = make_move(state, move, player)
            score = minimax(new_state, depth - 1, 'X')
            best_score = min(best_score, score)

        return best_score

board = ['X', 'X', ' ', 'O', 'O', ' ',
         ' ', ' ', ' ']

print("Best score:", minimax(board, 3, 'X'))
