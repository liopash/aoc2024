'''
File Loader Module
'''

from pathlib import Path

def get_input(file_name='input.txt'):
    """
    Returns the content of the specified input file.

    Parameters:
    file_name (str): The path to the input file to read. Can be relative or absolute.

    Returns:
    str: Content of the input file.
    """
    # Resolve the path to an absolute path
    file_path = Path(file_name).resolve()

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        content = ""
        print(f"File '{file_path}' not found.")
    except IOError as e:
        content = ""
        print(f"Error reading file '{file_path}': {e}")

    return content

