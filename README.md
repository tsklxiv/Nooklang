# Nook

Nook is a simple, concatenative programming language written in Python.

## Status

Nook is currently WIP. It lacks a lot of basic feature, and will need a quite long time of development.

For now, Nook is enough to make very simple tests.

## Installation

First, install `python` (Python 3) and `pip`. (https://www.python.org)

Next, if you want to compile Nook to executable, install [Nuitka](https://nuitka.net) through `pip`:

```
pip3 install -U nuitka
```

Then, clone this repository:

```
git clone https://github.com/HoangTuan110/Nooklang
```

Finally, go to the cloned directory, and:
- If you want to compile the language, use:
		```
		chmod +x ./build_executable
		./build_executable
		```
	- Then, to run the language, use:
			```
			./nook
			```
- If you just want to run the language without compiling it, use:
		```
		python3 src/main.py
		```

## How to use

If you don't feed any file to the CLI argument, like this:

```
./nook
```

Nook will trigger the REPL by default.

If so, Nook will tried to run that file.

## Examples

You can view examples in the `examples` directory.

## License

MIT
