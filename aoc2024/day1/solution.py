"""
Solution for Day 1 of the Advent of Code 2024.
"""

from pathlib import Path
from aoc2024.utils.file_loader import get_input


def parse_input(content):
    """
    Parses the input content into two lists of integers representing the two columns.

    Parameters:
    content (str): The input file content as a string.

    Returns:
    tuple[list[int], list[int]]: Two lists of integers, representing the first and second columns.
    """
    first_column = []
    second_column = []

    for line in content.splitlines():
        first, second = map(int, line.split('   '))
        first_column.append(first)
        second_column.append(second)

    return first_column, second_column


def calculate_sum_of_differences(first_column, second_column):
    """
    Calculates the sum of absolute differences between two sorted lists.

    Parameters:
    first_column (list[int]): The first column of integers.
    second_column (list[int]): The second column of integers.

    Returns:
    int: The sum of absolute differences.
    """
    sorted_first = sorted(first_column)
    sorted_second = sorted(second_column)

    return sum(abs(a - b) for a, b in zip(sorted_first, sorted_second))


def calculate_similarity_score(first_column, second_column):
    """
    Calculates the similarity score between two lists.

    The similarity score is the sum of each number in the first list multiplied
    by its count in the second list.

    Parameters:
    first_column (list[int]): The first column of integers.
    second_column (list[int]): The second column of integers.

    Returns:
    int: The similarity score.
    """

    similarity_score = 0
    for a in sorted(first_column):
        similarity_score += a * second_column.count(a)

    return similarity_score


def main():
    """
    Main function to execute the solution logic.
    """
    # Load and parse the input
    input_file = Path(__file__).resolve().parent / 'input.txt'
    content = get_input(input_file)
    first_column, second_column = parse_input(content)

    # Calculate results
    sum_of_diff = calculate_sum_of_differences(first_column, second_column)
    similarity_score = calculate_similarity_score(first_column, second_column)

    # Print results
    print("Sum of absolute differences:", sum_of_diff)
    print("Similarity score:", similarity_score)


if __name__ == "__main__":
    main()
