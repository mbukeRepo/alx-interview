#!/usr/bin/python3
""" log parsing with python """

from sys import stdin

size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def print_stats():
    print("File size: {}".format(size))
    for status in sorted(status_codes.keys()):
        if status_codes[status]:
            print("{}: {}".format(status, status_codes[status]))

if __name__ == "__main__":
    count = 0
    try:
        for line in stdin:
            try:
                components = line.split()
                size += int(components[-1])
                if components[-2] in status_codes:
                    status_codes[components[-2]] += 1
            except:
                pass
            if count == 9:
                print_stats()
                count = -1
            count += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
