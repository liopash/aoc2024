'''
Day 6 solution - walk the guard
'''
from pathlib import Path
from aoc2024.utils.file_loader import get_input

def create_matrix(text):
    lines = text.split('\n')
    matrix = [list(line) for line in lines]
    return matrix

class LoopDetectedError(Exception):
    pass

def walk_guard(matrix):
    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction = 0  # Starting direction: up

    path = []
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == '^':
                x, y = i, j
                break

    path.append((x, y, direction))


    visited_states = set()
    visited_states.add((x, y, direction))

    while True:
        next_x, next_y = x + directions[direction][0], y + directions[direction][1]

        if next_x < 0 or next_x >= len(matrix) or next_y < 0 or next_y >= len(matrix[0]):
            break

        if matrix[next_x][next_y] == '#' or matrix[next_x][next_y] == 'O':
            direction = (direction + 1) % 4
        else:
            x, y = next_x, next_y
            path.append((x, y, direction))

            if (x, y, direction) in visited_states:
                raise LoopDetectedError

            visited_states.add((x, y, direction))

    return path

def test_obstacles_for_loops(matrix, visited_path):
    """
    Test if placing an obstacle at each position in the path causes a loop.

    :param matrix: The original matrix.
    :param visited_path: The path of the guard (array of coordinates (x, y, direction)).
    :return: The number of obstacles that cause a loop.
    """
    obstacles = set()

    for x, y, _ in visited_path:
        modified_matrix = [row[:] for row in matrix]
        if modified_matrix[x][y] != '^':
            modified_matrix[x][y] = 'O'
        # print("Modified matrix:")
        # for row in modified_matrix:
        #     print(''.join(row))

        try:
            walk_guard(modified_matrix)
        except LoopDetectedError:
            obstacles.add((x, y))

    return len(obstacles)


def main():
    """
    Main function
    """
    input_file = Path(__file__).resolve().parent / 'input.txt'
    matrix = create_matrix(get_input(input_file))
    print("Initial matrix:")
    for row in matrix:
        print(''.join(row))
    print("\nGuard's path:")
    path = walk_guard(matrix)
    guard_steps = len(path)
    print("Guard's steps:", guard_steps)

    print("Part 2:")
    loop_count = test_obstacles_for_loops(matrix, path)
    print("Number of loops:", loop_count)

if __name__ == "__main__":
    main()