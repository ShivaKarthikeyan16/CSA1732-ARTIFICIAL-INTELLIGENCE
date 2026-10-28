from collections import deque

def water_jug_problem(x, y, z):
    queue = deque([(0, 0, [])])
    visited = set()

    while queue:
        a, b, steps = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))

        if a == z or b == z:
            return steps

        queue.append((x, b, steps + ["Fill jug 1"]))
        queue.append((a, y, steps + ["Fill jug 2"]))
        queue.append((0, b, steps + ["Empty jug 1"]))
        queue.append((a, 0, steps + ["Empty jug 2"]))

        amount = min(a, y - b)
        queue.append((a - amount, b + amount,
                      steps + ["Pour jug 1 into jug 2"]))

        amount = min(x - a, b)
        queue.append((a + amount, b - amount,
                      steps + ["Pour jug 2 into jug 1"]))

    return None


steps = water_jug_problem(4, 3, 2)

if steps is not None:
    print("\n".join(steps))
else:
    print("No solution found.")
