# shim to support 'import messages'
from importlib import import_module

# Try to import functions from 38.5_messages.py
try:
    _mod = import_module('38.5_messages')  # unconventional, may fail due to name
except ModuleNotFoundError:
    # Fallback: define directly if unusual filename can't be imported
    def hello():
        print("Hello! Have a nice day!")
    def bye():
        print("Bye! Have a wonderful time!")
else:
    hello = getattr(_mod, 'hello')
    bye = getattr(_mod, 'bye')
