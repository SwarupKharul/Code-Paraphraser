from utility import print_function_name, logger

# Keywords in python
keywords = [
        "if",
        "else",
        "elif",
        "while",
        "for",
        "def",
        "class",
        "return",
        "True",
        "False",
        "None",
        "print",
        "input",
    ]


# Filter out multi-line comments
@print_function_name
def filter_multiline_comments(code:str) -> tuple:
    comments = []

    # get the docstring and store it in comments
    new_code = code.split('"""')
    only_code = new_code[0]
    if len(new_code) > 1:
        for i in range(1, len(new_code), 2):
            comments.append(new_code[i])
        for i in range(2, len(new_code), 2):
            only_code += new_code[i]
    return (only_code, comments)


# Filter out comments
@print_function_name
def filter_comments(tokens: list) -> tuple:
    comments = []
    for token in tokens:
        if token.startswith("#"):
            comments.append(token)
    for comment in comments:
        tokens.remove(comment)
    return tokens, comments

# Filter out keywords
@print_function_name
def filter_keywords(tokens) -> list:
    return [token for token in tokens if not token in keywords]



