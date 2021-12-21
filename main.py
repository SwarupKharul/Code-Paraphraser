from tokenize import word_tokenize
from rename import rename
import sys

# clear log.txt
with open("log.txt", "w") as f:
    f.write("")

# get name of file from end of command line
try:
    file_name = sys.argv[1]
except IndexError:
    file_name = "test.py"

# function to detect the language
def detect_language(file_name: str) -> str:
    ext = file_name.split(".")[-1]
    if ext == "py":
        return "python"
    elif ext == "java":
        return "java"
    elif ext == "c":
        return "c"
    elif ext == "cpp":
        return "cpp"
    elif ext == "cs":
        return "cs"
    elif ext == "js":
        return "js"
    elif ext == "html":
        return "html"
    elif ext == "css":
        return "css"
    elif ext == "sql":
        return "sql"
    elif ext == "sh":
        return "sh"
    elif ext == "go":
        return "go"
    elif ext == "php":
        return "php"
    elif ext == "py":
        return "py"
    else:
        return "unknown"

# read a code snippet from test.py
with open(file_name, "r") as f:
    example_code_snippet = f.read()

language = detect_language(file_name)

words = word_tokenize(example_code_snippet,language)

rename(words)
