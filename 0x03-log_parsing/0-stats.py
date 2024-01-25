#!/usr/bin/python3
import sys
import signal
from datetime import datetime


def print_stats(total_size, status_counts):
    print("File size: {}".format(total_size))
    for code, count in sorted(status_counts.items()):
        print("{}: {}".format(code, count))


def handle_interrupt(signal, frame):
    print_stats(total_size, status_counts)
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)

line_count = 0
total_size = 0
status_counts = {}

try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        if len(parts) >= 7:
            ip, _, _, _, _, status_code, size = parts[:7]
            if status_code.isdigit():
                status_code = int(status_code)
                size = int(size)
                line_count += 1
                total_size += size
                status_counts[status_code] = status_counts.get(
                    status_code, 0) + 1
                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)
except KeyboardInterrupt:
    pass

print_stats(total_size, status_counts)
