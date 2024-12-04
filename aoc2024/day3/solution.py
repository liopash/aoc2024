'''
Day 3 - Solution
'''
import re

from pathlib import Path
from aoc2024.utils.file_loader import get_input

def find_mul_patterns(text):
    pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    return pattern.findall(text)

def add_newline_before_do_and_dont(text):
    text = text.replace('\n', '')
    modified_text = re.sub(r'(do\(\)|don\'t\(\))', r'\n\1', text)
    return modified_text

def find_mul_patterns_without_dont_lines(text):
    '''
    use add newline before do and dont and then find mul patterns
    skip lines which are starting with dont
    '''
    modified_text = add_newline_before_do_and_dont(text)
    lines = modified_text.splitlines(True)

    mul_patterns = []
    for line in lines:
        if line.startswith("don't"):
            continue
        mul_patterns.extend(find_mul_patterns(line))

    return mul_patterns

def main():
    """
    Main function to execute the solution logic.
    """
    # Load and parse the input
    input_file = Path(__file__).resolve().parent / 'input.txt'
    content = get_input(input_file)

    found_patterns = find_mul_patterns(content)
    total_sum = sum(int(a) * int(b) for a, b in found_patterns)
    print("Total sum of 'mul' patterns:", total_sum)

    do_total_sum = sum(int(a) * int(b) for a, b in find_mul_patterns_without_dont_lines(content))
    print("Total sum of 'mul' patterns without 'don't':", do_total_sum)

if __name__ == "__main__":
    main()
