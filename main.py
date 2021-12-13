from tokenize import word_tokenize

# clear log.txt
with open('log.txt', 'w') as f:
    f.write('')

example_code_snippet = """
# This is a comment
def example_function(param1 = 60, param2 = 50):
    string = " this is a string "
    print(param1)
    print(param2)
"""
print(word_tokenize(example_code_snippet, test=True))


