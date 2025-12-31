import math

class Histogram:
    def __init__(self, bins=20):
        self.buckets = {}
        self.count = 0
        self.min = float('inf')
        self.max = 0
        self.sum = 0

    def add(self, value):
        if value < 0: return
        self.count += 1
        self.sum += value
        if value < self.min: self.min = value
        if value > self.max: self.max = value

        # simple logarithmic binning
        b = int(math.log10(value + 1) * 10)
        self.buckets[b] = self.buckets.get(b, 0) + 1

    def get_percentile(self, p):
        if not self.count: return 0
        sorted_items = sorted(self.buckets.items())
        target = (p / 100.0) * self.count
        current = 0
        for b, count in sorted_items:
            current += count
            if current >= target:
                return 10 ** (b / 10.0) - 1
        return self.max
