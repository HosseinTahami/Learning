"""
BaseException
 ├── BaseExceptionGroup
 ├── GeneratorExit
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ExceptionGroup [BaseExceptionGroup]
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    └── RecursionError
      ├── StopAsyncIteration
      ├── StopIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── BytesWarning
           ├── DeprecationWarning
           ├── EncodingWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── PendingDeprecationWarning
           ├── ResourceWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UnicodeWarning
           └── UserWarning
"""

"""
Error Types:
1. SyntaxError
2. ZeroDivisionError
3. TypeError
4. FileNotFoundError
5. IndentationError
6. NameError
7. ValueError
"""

"""
SyntaxError:
Missing parentheses in call to 'print'. Did you mean print(...)?
"""
# print "Hello"

"""
ZeroDivisionError:
division by zero
"""
# 2 / 0

"""
TypeError:
unsupported operand type(s) for -: 'int' and 'str'
"""
# 2 * 3 - '4'

"""
FileNotFoundError:
[Errno 2] No such file or directory: 'Text.txt'
"""
# f = open("Text.txt", 'r')

"""
NameError:
name 'a' is not defined
"""
# print(a)

"""
ValueError:
invalid literal for int() with base 10: 'forty-two'
"""
# int("forty-two")


name = "amir"
try:
    name = str.upper(name)
except TypeError:
    print("Your name must be string !")
else:
    print("Done!")
finally:
    print("Will be run no matter what happens !")


name = 32
try:
    name = str.upper(name)
except TypeError:
    print("Your name must be string !")
else:
    print("Done!")
finally:
    print("Will be run no matter what happens !")

x = 2
if x == 2:
    raise ValueError('variable cant be two !')
    raise Exception('Variable cant be two !')
