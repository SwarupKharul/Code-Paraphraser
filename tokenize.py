# Functions for tokenizing a code snippet
import re
from utility import print_function_name, logger
from languages import *


# Tokenize snippet
@print_function_name
def tokenize_lines(code: str) -> list:
    lines = code.split("\n")
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


def find_strings(line: str) -> list:
    strings = []
    # Make an array of all the strings in the line
    # regular expression for " " in a line
    strings += re.findall(r"\" ?.* ?\"", line)
    # regular expression for ' ' in a line
    strings += re.findall(r"\' ?.* ?\'", line)
    print(strings)
    return strings


# # Filter out strings
@print_function_name
def filter_strings(tokens) -> list:
    new_tokens = []
    for token in tokens:
        temp = token
        for string in find_strings(temp):
            token = temp.replace(string, " ")
            logger(message=f"\n{temp} replaced with {token}")
        new_tokens.append(token)
    logger(message=f"\n\nTokens: {new_tokens}")
    return new_tokens


# Filter out numbers
@print_function_name
def filter_numbers(tokens) -> list:
    return [token for token in tokens if not token.isdigit()]


# Filter all above functions
def word_tokenize(code, language) -> set:
    language_function = eval(f"{language}")
    code, multiline_comments = language_function.filter_multiline_comments(code)
    tokens = tokenize_lines(code)
    tokens, comments = language_function.filter_comments(tokens)
    tokens = filter_strings(tokens)
    tokens = tokenize_words(tokens)
    tokens = filter_empty_tokens(tokens)
    tokens = filter_numbers(tokens)
    tokens = language_function.filter_keywords(tokens)
    return set(tokens)
