# Nook

Nook is a simple, concatenative programming language written in Python.

## Status

Nook is stable and ready to use.

## Installation

### Build the language as an executable

```sh
pip3 install -U nuitka # Install Nuitka
git clone https://github.com/HoangTuan110/Nooklang
cd Nooklang
chmod +x ./build_executable
./build_executable
./nook
```

### Simply run the language

```sh
git clone https://github.com/HoangTuan110/Nooklang
cd Nooklang
python ./src/main.py
```

## How to use

If you don't feed any file to the CLI argument, like this:

```
./nook
```

Then Nook will trigger the REPL by default.

If so, Nook will tried to run that file.

## Examples

You can view examples in the `examples` directory.

## License

MIT
