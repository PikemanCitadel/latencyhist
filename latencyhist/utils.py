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

def parse_time_unit(val, unit):
    # convert everything to ms
    # print(f"debug: val={val} unit={unit}")
    mult = 1.0
    u = unit.lower()
    if u == 's': mult = 1000.0
    elif u == 'us' or u == 'μs': mult = 0.001
    elif u == 'ns': mult = 0.000001
    
    return float(val) * mult
