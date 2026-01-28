import re

# common patterns to save people from writing regex
PRESETS = {
    'nginx': r'\[.*?\] \".*?\" \d{3} .*? (\d+\.\d+)$',
    'nginx_combined': r'rt=([\d\.]+)',
    'apache': r'\" \d{3} \d+ (\d+)$' # apache duration is usually microseconds
}

class LogParser:
    def __init__(self, pattern, field_id=None):
        self.pattern = PRESETS.get(pattern, pattern)
        self.field_id = field_id
        
        try:
            self.rx = re.compile(self.pattern)
        except re.error as e:
            print(f"invalid regex: {e}")
            raise

    def extract_value(self, line):
        match = self.rx.search(line)
        if not match:
            return None
        
        try:
            # if user gave a name like (?P<latency>...), use it
            if self.field_id and not self.field_id.isdigit():
                raw_val = match.group(self.field_id)
            else:
                # default to first group or specific index
                idx = int(self.field_id) if self.field_id else 1
                raw_val = match.group(idx)
            
            return float(raw_val)
        except (ValueError, IndexError, KeyError):
            # happens if log line is truncated or field is missing
            return None

# FIXME: this parser is quite slow for 100k+ lines/sec. 
# Should probably check if we can use string.split() if it's a simple space-separated log.
