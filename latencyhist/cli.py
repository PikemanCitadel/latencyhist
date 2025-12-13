import sys
import argparse
from latencyhist.parser import LogParser
from latencyhist.stats import Collector

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--format', default='nginx', help='log format (nginx, apache, or custom regex)')
    parser.add_argument('--field', default='request_time', help='field to extract')
    args = parser.parse_args()

    log_parser = LogParser(args.format, args.field)
    collector = Collector()

    try:
        for line in sys.stdin:
            val = log_parser.parse_line(line)
            if val is not None:
                collector.add(val)
                # print(f"debug: {val}")
    except KeyboardInterrupt:
        collector.print_summary()
        sys.exit(0)

if __name__ == '__main__':
    main()
