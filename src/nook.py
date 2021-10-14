"""

    The Nook Programming Language.

"""

# Consts
WHITESPACE = " \t\r\f"
VERSION = "0.1"

# Lambdas
numeric = lambda c: c.isnumeric()
identifier = lambda c: (c.isalpha() or c.isascii()) and c not in WHITESPACE
report = lambda msg, line, pos: print(f"Error: {msg}" + ("" if (line == None) else f"\nAt line {line}, position {pos}"))

# Helper functions
def set_env(env: dict, name: str, value) -> dict:
    env[name] = value
    return env

def pop(stack: list):
    if len(stack) == 0:
        report("Stack empty", None, 0)
        return 0
    else:
        return stack.pop()

def peek(stack: list):
    if len(stack) == 0:
        report("Stack empty", None, 0)
        return 0
    else:
        return stack[-1]

def consume(condition, inpt: str, pos: int):
    prev_pos = pos
    pos += 1

    while pos < len(inpt) and condition(inpt[pos]):
        pos += 1

    return (inpt[prev_pos:pos], pos)

def run(inpt: str, stack: list, env: dict):
    c = 0 # Pointer
    vc = 0 # Virtual pointer
    line = 1 # Line

    while c < len(inpt):
        current = inpt[c]

        # Consume positive numbers
        if numeric(current):
            number, c = consume(lambda c: numeric(c), inpt, c)
            number = int(number)
            vc = c
            stack.append(number)
        # Consume negative numbers (_500 = -500)
        elif current == "_":
            c += 1
            number, c = consume(lambda c: numeric(c), inpt, c)
            number = int(number) * -1
            vc = c
            stack.append(number)
        elif current in WHITESPACE:
            vc += 1
            c += 1
        elif current == "#":
            while c < len(inpt) and inpt[c] != "\n":
                c += 1
        elif current == "\n":
            vc = 0
            line += 1
            c += 1
        # String
        elif current == "{": 
            c += 1
            string, c = consume(lambda c: c != "}", inpt, c)
            stack.append(string)
            c += 1
            vc = c 
        elif identifier(current):
            name, c = consume(lambda c: identifier(c), inpt, c)
            vc = c

            if name in env:
                env[name]()
            else:
                report(f"Not defined: {repr(name)}", line, vc) 
        else:
            report(f"Invalid character: {repr(current)}", line, vc)
            vc += 1
            c += 1
    
    return stack, env

# Run the input without worrying about stack and environment
def run_script(script: str):
    stack, env = init_env()
    stack, env = run(script, stack, env)

# Initialize environment
def init_env(stack: list = [], env: dict = {}) -> tuple:
    env = {
        "v": lambda: print(stack),
        "w": lambda: print(pop(stack)),
        "p": lambda: print(peek(stack)),
        ".": lambda: pop(stack),
        "+": lambda: stack.append(stack.pop() + stack.pop()), 
        "-": lambda: stack.append(stack.pop() - stack.pop()), 
        "*": lambda: stack.append(stack.pop() * stack.pop()),
        "/": lambda: stack.append(stack.pop() // stack.pop()),
        "%": lambda: stack.append(stack.pop() % stack.pop()),
        "s": lambda: set_env(env, str(pop(stack)), pop(stack)),
        "l": lambda: stack.append(env[str(pop(stack))]),
        "x": lambda: run_script(str(pop(stack))),
    }

    return (stack, env)
