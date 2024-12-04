import pytest
from aoc2024.day1.solution import (
    parse_input,
    calculate_sum_of_differences,
    calculate_similarity_score,
)


@pytest.fixture
def test_data():
    """
    Fixture to provide test data to multiple tests.
    """
    test_content = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    first_column = [3, 4, 2, 1, 3, 3]
    second_column = [4, 3, 5, 3, 9, 3]
    return test_content, first_column, second_column


def test_parse_input(test_data):
    """
    Test the parse_input function to ensure it correctly parses content into two lists.
    """
    test_content, first_column, second_column = test_data
    parsed_first_column, parsed_second_column = parse_input(test_content)
    assert parsed_first_column == first_column
    assert parsed_second_column == second_column


def test_calculate_sum_of_differences(test_data):
    """
    Test the calculate_sum_of_differences function for correct results.
    """
    _, first_column, second_column = test_data
    result = calculate_sum_of_differences(first_column, second_column)
    # Sorted first column: [1, 2, 3, 3, 3, 4]
    # Sorted second column: [3, 3, 3, 4, 5, 9]
    # Absolute differences: |1-3| + |2-3| + |3-3| + |3-4| + |3-5| + |4-9|
    # = 2 + 1 + 0 + 1 + 2 + 5 = 11
    assert result == 11


def test_calculate_similarity_score(test_data):
    """
    Test the calculate_similarity_score function for correct results.
    """
    _, first_column, second_column = test_data
    result = calculate_similarity_score(first_column, second_column)
    assert result == 31  # Based on standard calculation logic.
