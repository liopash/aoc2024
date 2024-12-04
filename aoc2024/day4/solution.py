'''
Day 4: Word Search
'''
from pathlib import Path
from aoc2024.utils.file_loader import get_input

def search_word(matrix, word):
    count = 0
    rows, cols = len(matrix), len(matrix[0])
    directions = [
        (1, 0),  # Horizontal right
        (-1, 0),  # Horizontal left
        (0, 1),  # Vertical down
        (0, -1),  # Vertical up
        (1, 1),  # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
        (-1, -1)  # Diagonal up-left
    ]

    def check_direction(x, y, dx, dy, word):
        for i in range(len(word)):
            if not (0 <= x < rows and 0 <= y < cols and matrix[x][y] == word[i]):
                return False
            x += dx
            y += dy
        return True

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_direction(i, j, dx, dy, word):
                    # print(f"Word '{word}' found starting at ({i}, {j}) in direction ({dx}, {dy})")
                    count += 1

    print(f"Word '{word}' found {count} times in the matrix")

    def find_mas_patterns():
        patterns = []
        for i in range(rows - 2):
            for j in range(cols - 2):
                sub_matrix = [matrix[i][j:j + 3], matrix[i + 1][j:j + 3], matrix[i + 2][j:j + 3]]
                if (sub_matrix[0][0] == 'M' and sub_matrix[0][2] == 'S' and sub_matrix[1][1] == 'A' and sub_matrix[2][0] == 'M' and sub_matrix[2][2] == 'S') or \
                   (sub_matrix[0][0] == 'S' and sub_matrix[0][2] == 'M' and sub_matrix[1][1] == 'A' and sub_matrix[2][0] == 'S' and sub_matrix[2][2] == 'M') or \
                   (sub_matrix[0][0] == 'M' and sub_matrix[0][2] == 'M' and sub_matrix[1][1] == 'A' and sub_matrix[2][0] == 'S' and sub_matrix[2][2] == 'S') or \
                   (sub_matrix[0][0] == 'S' and sub_matrix[0][2] == 'S' and sub_matrix[1][1] == 'A' and sub_matrix[2][0] == 'M' and sub_matrix[2][2] == 'M'):
                    patterns.append((i, j))
        return patterns

    mas_patterns = find_mas_patterns()
    print(f"'MAS' pattern found {len(mas_patterns)} times in the matrix")

def main():
    """
    Main function to execute the solution logic.
    """
    input_file = Path(__file__).resolve().parent / 'input.txt'
    content = get_input(input_file)
    matrix = content.splitlines()

    search_word(matrix, "XMAS")

if __name__ == "__main__":
    main()