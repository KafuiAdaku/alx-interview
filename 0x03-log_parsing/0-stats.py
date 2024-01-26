#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""
import sys
import datetime
import re


def parse_log_line(line):
    """Returns a regular expression match object"""
    pattern = (
        r"^\d+\.\d+\.\d+\.\d+ - "
        r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{1,6}\] "
        r"\"GET /projects/260 HTTP/1.1\" (\d{3}) (\d{1,4})$"
        )
    regex = re.compile(pattern)
    mo = regex.search(line)
    return mo


def process_log():
    """Processes parsed log"""
    count = 0
    code_list = []
    stat_code_cnt = {}
    cum_size = 0

    try:
        for line in sys.stdin:
            count += 1
            line = line.strip()
            if line:
                log_mo = parse_log_line(line)
                if log_mo and type(int(log_mo.group(1))) is int:
                    status = log_mo.group(1)
                    file_size = int(log_mo.group(2))
                    cum_size += file_size
                    stat_code_cnt[status] = stat_code_cnt.get(status, 0) + 1

            if count == 10:
                count = 0
                print(f"File size: {cum_size}")
                cum_size = 0
                for k in sorted(stat_code_cnt.keys()):
                    print(f"{k}: {stat_code_cnt[k]}")
    except KeyboardInterrupt:
        print(f"File size: {cum_size}")
        for k in sorted(stat_code_cnt.keys()):
            print(f"{k}: {stat_code_cnt[k]}")


if __name__ == "__main__":
    process_log()
