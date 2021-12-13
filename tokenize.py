""" Functions for tokenizing a code snippet """
import re

# Keywords in python
keywords = ['if', 'else', 'elif', 'while', 'for', 'def', 'class', 'return', 'True', 'False', 'None', 'print', 'input']

# Logger function
def logger(message):
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
def tokenize_lines(code):
    lines = code.split('\n')
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if line]
    return lines

# Split the code snippets on each space so that each word is a token
@print_function_name
def tokenize_words(code):
    tokens = []
    for line in code:
        words = line.split(' ')
        for word in words:
            tokens.append(word)
    return tokens

# Filter out empty tokens
@print_function_name
def filter_empty_tokens(tokens):
    return [token for token in tokens if token]

# Filter out comments
@print_function_name
def filter_comments(tokens):
    return [token for token in tokens if not token.startswith('#')]

def find_strings(code):
    strings = []
    # Make an array of all the strings in the code
    for line in code:
        strings += re.findall(r'"[^"]*"', line)
    print(strings)
    return strings

# Filter out strings
@print_function_name
def filter_strings(tokens):
    for token in tokens:
        for string in find_strings(token):
            token.replace(string, " ")
    return tokens

# Filter out numbers
@print_function_name
def filter_numbers(tokens):
    return [token for token in tokens if not token.isdigit()]

# Filter out keywords
@print_function_name
def filter_keywords(tokens):
    return [token for token in tokens if not token in keywords]

# Remove brackets, paranthasis, and colons from each token
@print_function_name
def remove_brackets(tokens):
    remove_brackets = ['(', ')', '[', ']', '{', '}', ':']
    for token in tokens:
        for bracket in remove_brackets:
            token = token.replace(bracket, '')
    return tokens

# Filter all above functions
def word_tokenize(code, test = False):
    global debug
    debug = test
    tokens = tokenize_lines(code)
    tokens = filter_comments(tokens)
    tokens = filter_strings(tokens)
    tokens = tokenize_words(tokens)
    tokens = filter_empty_tokens(tokens)
    tokens = filter_numbers(tokens)
    tokens = filter_keywords(tokens)
    tokens = remove_brackets(tokens)
    return tokens