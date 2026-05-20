import sys
import argparse
import time
from latencyhist.parser import LogParser
from latencyhist.stats import Histogram

def main():
    p = argparse.ArgumentParser(description="pipe logs here to see latency distribution")
    p.add_argument('--format', default='nginx', help='log format name or raw regex')
    p.add_argument('--field', help='field name or regex group index')
    p.add_argument('--interval', type=int, default=0, help='refresh interval in seconds (0 to only print at end)')
    p.add_argument('--buckets', type=int, default=20, help='number of histogram buckets')
    args = p.parse_args()

    # if it's nginx/apache we usually know where the time is if not specified
    field = args.field
    if not field:
        field = 'request_time' if args.format == 'nginx' else '1'

    parser = LogParser(args.format, field)
    hist = Histogram(buckets=args.buckets)

    last_refresh = time.time()

    try:
        for line in sys.stdin:
            if not line:
                continue
            
            val = parser.extract_value(line)
            if val is not None:
                hist.add(val)
            
            if args.interval > 0 and (time.time() - last_refresh) > args.interval:
                # clear screen logic should go here maybe?
                print("\033[H\033[J", end="") 
                hist.render()
                last_refresh = time.time()

    except KeyboardInterrupt:
        pass
    
    print("\nFinal Summary:")
    hist.render()

if __name__ == '__main__':
    main()
