from queue import PriorityQueue

goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def heuristic(state):
    distance = 0

    for i in range(3):
        for j in range(3):
            tile = state[i * 3 + j]

            if tile != 0:
                x = (tile - 1) // 3
                y = (tile - 1) % 3

                distance += abs(x - i) + abs(y - j)

    return distance


def successors(state):
    result = []
    i = state.index(0)

    if i % 3 != 0:
        new_state = list(state)
        new_state[i], new_state[i - 1] = new_state[i - 1], new_state[i]
        result.append(tuple(new_state))

    if i % 3 != 2:
        new_state = list(state)
        new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
        result.append(tuple(new_state))

    if i // 3 != 0:
        new_state = list(state)
        new_state[i], new_state[i - 3] = new_state[i - 3], new_state[i]
        result.append(tuple(new_state))

    if i // 3 != 2:
        new_state = list(state)
        new_state[i], new_state[i + 3] = new_state[i + 3], new_state[i]
        result.append(tuple(new_state))

    return result


def solve(initial_state):
    frontier = PriorityQueue()
    frontier.put((heuristic(initial_state), initial_state))
    explored = set()

    while not frontier.empty():
        _, state = frontier.get()

        if state == goal_state:
            return True

        if state in explored:
            continue

        explored.add(state)

        for successor in successors(state):
            if successor not in explored:
                priority = heuristic(successor) + len(explored)
                frontier.put((priority, successor))

    return False


initial_state = (2, 8, 3, 1, 6, 4, 7, 0, 5)

if solve(initial_state):
    print("The puzzle is solvable!")
else:
    print("The puzzle is unsolvable.")
