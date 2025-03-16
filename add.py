#!/usr/bin/env python3

from db_utils import DBManager
from hash_it import hash_the_file
from datetime import datetime
import argparse

def main():
    parser = argparse.ArgumentParser(description="Add files to the integrity checker database.")
    parser.add_argument("filepaths", type=str, help="Comma-separated list of file paths to add.")
    args = parser.parse_args()
    file_list = args.filepaths.split(",")

    adder = DBManager()

    for file in file_list:
        filehash = hash_the_file(file)
        adder.add(file, filehash)

        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        log_entry = f"{timestamp} [ADDED] {file} - {filehash}\n"

        with open('logs/adder.log', 'a') as addlog:
            addlog.write(log_entry)


if __name__ == '__main__':
    main()
