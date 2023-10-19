#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def append_write(filename="", text=""):
    """
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
