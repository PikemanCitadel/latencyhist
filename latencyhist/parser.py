import re

class LogParser:
    """Handles extraction of numeric values from text streams."""
    def __init__(self, fmt, field):
        self.fmt = fmt
        self.field = field
        self._rx = self._build_regex()

    def _build_regex(self):
        if self.fmt == 'nginx':
            # very basic nginx default log format
            return re.compile(r'rt=(\d+\.\d+)')
        return re.compile(self.fmt)

    def extract_value(self, line):
        m = self._rx.search(line)
        if m:
            try:
                return float(m.group(1))
            except (ValueError, IndexError):
                return None
        return None
