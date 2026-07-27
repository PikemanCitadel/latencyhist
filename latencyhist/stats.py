import math
import shutil
from latencyhist.utils import get_color, TERM_RESET

class Histogram:
    """Collects samples and renders a text-based histogram to stdout."""
    def __init__(self, bin_width=50):
        self.data = []
        self.bin_width = bin_width
        self.count = 0
        self.min = float('inf')
        self.max = 0
        self.sum = 0

    def update(self, val):
        if val is None: return
        self.data.append(val)
        self.count += 1
        self.sum += val
        if val < self.min: self.min = val
        if val > self.max: self.max = val

    def get_percentile(self, p):
        if not self.data: return 0
        s = sorted(self.data)
        idx = int(len(s) * (p / 100.0))
        return s[min(idx, len(s) - 1)]

    def render(self):
        if not self.data:
            print("No data yet...")
            return

        cols, _ = shutil.get_terminal_size((80, 20))
        # reserve space for labels
        bar_max_width = cols - 25
        
        num_bins = 15
        r_min, r_max = self.min, self.max
        if r_min == r_max: r_max = r_min + 1
        
        step = (r_max - r_min) / num_bins
        bins = [0] * num_bins

        for v in self.data:
            idx = int((v - r_min) / step)
            if idx >= num_bins: idx = num_bins - 1
            bins[idx] += 1

        max_bin = max(bins) if bins else 1
        
        print(f"\nSummary: n={self.count} min={self.min:.2f} max={self.max:.2f} avg={self.sum/self.count:.2f}")
        print(f"p50: {self.get_percentile(50):.2f}ms  p95: {self.get_percentile(95):.2f}ms  p99: {self.get_percentile(99):.2f}ms\n")

        for i in range(num_bins):
            start = r_min + (i * step)
            count = bins[i]
            bar_len = int((count / max_bin) * bar_max_width)
            
            # colorize based on latency - arbitrary thresholds but works for web apps
            color = TERM_RESET
            if start > 500: color = get_color('red')
            elif start > 200: color = get_color('yellow')
            
            bar = "█" * bar_len
            # show the bar even if count is small but > 0
            if count > 0 and bar_len == 0:
                bar = "▏"
                
            print(f"{start:7.1f} ms |{color}{bar}{TERM_RESET} {count}")

# TODO: maybe add a way to prune old data for long-running pipes
# right now it just grows until OOM if you leave it for days
