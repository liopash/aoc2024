'''
Day 5 solution
'''
from pathlib import Path
from aoc2024.utils.file_loader import get_input

def parse_rules_as_tuples(rules):
    '''
    Parse the rules as tuples
    '''
    rule_tuples = []
    for rule in rules.splitlines():
        rule = rule.split('|')
        rule_tuples.append((rule[0], rule[1]))
    return rule_tuples

def check_rules_apply(rules, input_line):
    '''
    Check if rules apply to the input line
    '''
    rule_set = set(rules)
    elements = input_line.split(',')

    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            pair = (elements[i], elements[j])
            if pair not in rule_set:
                return False

    return True

def find_middle_number(numbers):
    """
    Find the middle number of any odd-length list with three or more elements
    """
    if len(numbers) < 3 or len(numbers) % 2 == 0:
        raise ValueError("Input list must have an odd length of at least 3")

    middle_index = len(numbers) // 2
    return numbers[middle_index]

def evaluate_priorities(rules, line):
    """Evaluate priorities of numbers based on rules."""
    priority = {num: 0 for num in line}

    for before, after in rules:
        if before in priority and after in priority:
            priority[after] += 1

    return priority

def custom_sort(line, rules):
    """Sort the line based on rules."""
    priority = evaluate_priorities(rules, line)

    sorted_line = sorted(line, key=lambda x: priority[x])

    return sorted_line


def main():
    '''
    Main function
    '''
    input_file = Path(__file__).resolve().parent / 'input.txt'
    content = get_input(input_file)
    input_rules = Path(__file__).resolve().parent / 'input_rules.txt'
    rules = get_input(input_rules)
    # print(parse_rules_as_tuples(rules))

    valid_lines = []
    for line in content.splitlines():
        if check_rules_apply(parse_rules_as_tuples(rules), line):
            valid_lines.append(line)

    result = 0
    for line in valid_lines:
        numbers = list(map(int, line.split(',')))
        result += find_middle_number(numbers)

    print("Result part 1:", result)

    invalid_lines = []
    for line in content.splitlines():
        if not check_rules_apply(parse_rules_as_tuples(rules), line):
            invalid_lines.append(line)

    result = 0
    for line in invalid_lines:
        sorted_line = custom_sort(line.split(','), parse_rules_as_tuples(rules))
        result += find_middle_number([int(num) for num in sorted_line])

    print("Result part 2:", result)


if __name__ == '__main__':
    main()