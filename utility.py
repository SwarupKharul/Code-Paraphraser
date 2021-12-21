debug = True

# Logger function
def logger(message: str) -> None:
    with open("log.txt", "a") as f:
        f.write(message)


""" Make a decorator to log in a different file which function is being called
This is used for debugging and should be printed only when debug = True """


def print_function_name(func):
    def wrapper(*args, **kwargs):
        if debug:
            logger(f"\n\nCalling {func.__name__}")
            logger(f"\nTokens: {args[0]}")
        return func(*args, **kwargs)

    return wrapper