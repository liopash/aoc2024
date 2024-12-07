'''
Day 7
'''
from itertools import product
from pathlib import Path
from aoc2024.utils.file_loader import get_input

def generate_permutations(num_operators, operators):
    return list(product(operators, repeat=num_operators))

def evaluate_expression_left_to_right(numbers, operators):
    result = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i-1] == '+':
            result += numbers[i]
        elif operators[i-1] == '*':
            result *= numbers[i]
        # elif operators[i-1] == '/': # concat
        #     result = int(str(result) + str(numbers[i]))
    return result

def find_combination(numbers, target):
    num_operators = len(numbers) - 1
    operators = ['+', '*', '/']
    permutations = generate_permutations(num_operators, operators)

    for perm in permutations:
        if evaluate_expression_left_to_right(numbers, perm) == target:
            return True, target

    return False, target

def process_input(data):
    results = []
    for line in data.strip().split('\n'):
        parts = line.split(': ')
        target = int(parts[0])
        numbers = list(map(int, parts[1].split()))
        result = find_combination(numbers, target)
        results.append(result)
    return results
def main():
    '''
    Main function
    '''
    input_file = Path(__file__).resolve().parent / 'input.txt'
    content = get_input(input_file)
    # Sum all True results for part 2 uncomment concat operator
    results = process_input(content)
    print("Sum target of all True results:")
    print(sum(result[1] for result in results if result[0]))


if __name__ == '__main__':
    main()