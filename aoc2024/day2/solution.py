'''
Day 2

Problem:
This example data contains six reports each containing five levels.
The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:
The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
'''
from pathlib import Path

from aoc2024.utils.file_loader import get_input

def parse_input(content):
    """
    Parses the input content into a list of reports containing levels.

    Parameters:
    content (str): The input file content as a string.

    Returns:
    list[list[int]]: A list of reports, each containing a list of levels.
    """
    reports = []

    for line in content.splitlines():
        levels = list(map(int, line.split(' ')))
        reports.append(levels)

    return reports

def is_safe_report(report):
    """
    Checks if a report is safe based on the levels.

    A report is safe if the levels are either all increasing or all decreasing,
    and the difference between any two adjacent levels is between 1 and 3.

    Parameters:
    report (list[int]): The levels in the report.

    Returns:
    bool: True if the report is safe, False otherwise.
    """
    increasing = all(a < b for a, b in zip(report, report[1:]))
    decreasing = all(a > b for a, b in zip(report, report[1:]))

    if increasing or decreasing:
        for a, b in zip(report, report[1:]):
            if abs(a - b) < 1 or abs(a - b) > 3:
                return False
        return True

    return False

def dampener(line):
    """
    Check if a list of numbers can become strictly increasing or decreasing
    by removing at most one element, with the added condition that the
    differences between consecutive elements are between 1 and 3.

    Args:
        line (list): A list of numbers.

    Returns:
        bool: True if the list can become strictly increasing or decreasing
              by removing at most one element and satisfying the difference
              constraint, False otherwise.
    """
    def can_be_monotonic_with_constraints(line):
        return (
            all(a < b and 1 <= b - a <= 3 for a, b in zip(line, line[1:])) or
            all(a > b and 1 <= a - b <= 3 for a, b in zip(line, line[1:]))
        )

    for i in range(len(line)):
        if can_be_monotonic_with_constraints(line[:i] + line[i+1:]):
            return True

    return False


def main():
    """
    Main function to execute the solution logic.
    """
    input_file = Path(__file__).resolve().parent / 'input.txt'
    reports = parse_input(get_input(input_file))
    print(f"Number of reports: {len(reports)}")

    count_safe_reports = sum(is_safe_report(report) for report in reports)
    print(f"Number of safe reports: {count_safe_reports}")

    count_safe_reports = sum(dampener(report) for report in reports)
    print(f"Number of safe  reports: {count_safe_reports}")

if __name__ == "__main__":
    main()
