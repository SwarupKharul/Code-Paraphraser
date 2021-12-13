# Functions for tokenizing a code snippet 
import re

# Keywords in python
keywords = ['if', 'else', 'elif', 'while', 'for', 'def', 'class', 'return', 'True', 'False', 'None', 'print', 'input']

# Logger function
def logger(message: str) -> None:
    with open('log.txt', 'a') as f:
        f.write(message)

""" Make a decorator to log in a different file which function is being called
This is used for debugging and should be printed only when debug = True """
def print_function_name(func):
    def wrapper(*args, **kwargs):
        if debug:
            logger(f'\n\nCalling {func.__name__}')
            logger(f'\nTokens: {args[0]}')
        return func(*args, **kwargs)
    return wrapper


# Tokenize snippet
@print_function_name
def tokenize_lines(code: str) -> list:
    lines = code.split('\n')
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if line]
    return lines

# Split the code snippets on each space so that each word is a token
@print_function_name
def tokenize_words(code: list) -> list:
    tokens = []
    for line in code:
        tokens += re.findall(r"[\w']+", line)
    return tokens

# Filter out empty tokens
@print_function_name
def filter_empty_tokens(tokens: list) -> list:
    return [token for token in tokens if token]

# Filter out multi-line comments
def filter_multiline_comments(file: str = "test.py") -> list:
    comments = []
    # Read the file
    with open(file, 'r') as f:
        code = f.read()
    # get the docstring and store it in comments
    code = code.split('"""')
    new_code = code[0]
    if len(code) > 1:
        for i in range(1, len(code), 2):
            comments.append(code[i])
        for i in range(2, len(code), 2):
            new_code += code[i]
    return new_code, comments

# Filter out comments
@print_function_name
def filter_comments(tokens: list) -> list:
    comments = []
    for token in tokens:
        if token.startswith('#'):
            comments.append(token)
    for comment in comments:
        tokens.remove(comment)
    return tokens, comments

def find_strings(line: str) -> list:
    strings = []
    # Make an array of all the strings in the line
    # regular expression for " " in a line
    strings += re.findall(r'\" ?.* ?\"', line)
    # regular expression for ' ' in a line
    strings += re.findall(r'\' ?.* ?\'', line)
    print(strings)
    return strings

# # Filter out strings
@print_function_name
def filter_strings(tokens) -> list:
    new_tokens=[]
    for token in tokens:
        temp = token
        for string in find_strings(temp):
            token = temp.replace(string, " ")
            logger(message = f'\n{temp} replaced with {token}')
        new_tokens.append(token)
    logger(message = f'\n\nTokens: {new_tokens}')
    return new_tokens

# Filter out numbers
@print_function_name
def filter_numbers(tokens) -> list:
    return [token for token in tokens if not token.isdigit()]

# Filter out keywords
@print_function_name
def filter_keywords(tokens) -> list:
    return [token for token in tokens if not token in keywords]

# Filter all above functions
def word_tokenize(code, test = False) -> set:
    global debug
    debug = test
    code, multiline_comments = filter_multiline_comments()
    tokens = tokenize_lines(code)
    tokens, comments = filter_comments(tokens)
    tokens = filter_strings(tokens)
    tokens = tokenize_words(tokens)
    tokens = filter_empty_tokens(tokens)
    tokens = filter_numbers(tokens)
    tokens = filter_keywords(tokens)
    return set(tokens)