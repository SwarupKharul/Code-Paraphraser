# Funtion to rename the words 
import string
import random

# function to randomly generate a string of given string length
def random_string(word : str) -> str:
    string_length = len(word)
    """ Generate a random string of fixed length """
    res = ''.join(random.choices(string.ascii_lowercase + string.digits, k = string_length))
    return str(res)

# function to rename a word in a file
def rename_text(word: str, new_name: str, file_name: str = "test.py"):
    # Open the file
    file = open(file_name, "r+")
    # Read the file
    text = file.read()
    # expression to find word not embedded in another word
    text_pattern = re.compile(r'(\b|\[|\(|\{)' + word + r'(\b|\]|\)|\}|\:|\,|\;|\?|\!|\s|\.)')
    # Replace the word with the new name
    text = re.sub(text_pattern, r'\1' + new_name + r'\2', text)
    # Write the file
    file.seek(0)
    file.write(text)
    file.truncate()
    file.close()

# function to rename the words
def rename(words: list):
    for word in words:
        # Ask user for the new name
        new_name = input(f"Enter the new name for the word {word}: ")
        # Check if the new name is empty
        if new_name == "":
            # If empty, generate a random name
            new_name = random_string(word)
        # Rename the word
        rename_text(word, new_name)
    return words