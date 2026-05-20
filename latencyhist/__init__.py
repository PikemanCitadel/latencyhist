from latencyhist.stats import Calculator
from latencyhist.parser import LogParser

__version__ = "0.1.1"

# we'll need this to avoid deep imports in tests
__all__ = ["Calculator", "LogParser"]
