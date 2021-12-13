from tokenize import word_tokenize
from rename import rename

# clear log.txt
with open('log.txt', 'w') as f:
    f.write('')

# read a code snippet from test.py
with open('test.py', 'r') as f:
    example_code_snippet = f.read()


words = word_tokenize(example_code_snippet, test=True)
print(words)

rename(words)


