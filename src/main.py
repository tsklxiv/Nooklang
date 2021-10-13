"""

    The CLI part of Nook

"""
from nook import VERSION, init_env, run
from sys import argv

# REPL
def repl():
    print("The Nook Programming Language.")
    print(f"Version {VERSION}")

    stack, env = init_env()
    
    while True:
        stack, env = run(input(">> "), stack, env)

# Argument handler
def arg_handler():
    if len(argv) == 1:
        repl()
    else:
        content = open(argv[1]).read().strip().replace("\n", " \n ")
        stack, env = init_env()
        stack, env = run(content, stack, env)


if __name__ == "__main__":
    arg_handler()
