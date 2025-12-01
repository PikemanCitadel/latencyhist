import sys

TERM_RESET = "\033[0m"

COLORS = {
    'red': "\033[31m",
    'green': "\033[32m",
    'yellow': "\033[33m",
    'blue': "\033[34m",
    'dim': "\033[2m"
}

def get_color(name):
    if not sys.stdout.isatty():
        return ""
    return COLORS.get(name, "")

