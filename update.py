#!/usr/bin/env python3

from datetime import datetime
from db_utils import DBManager
from hash_it import hash_the_file
import argparse

def main():
    parser = argparse.ArgumentParser(description="Update files in the integrity checker database.")
    parser.add_argument("filepaths", type=str, help="Comma-separated list of file paths to update.")
    args = parser.parse_args()
    file_list = args.filepaths.split(",")

    updater = DBManager()
    for file in file_list:
        oldhash = updater.read(file)
        newhash = hash_the_file(file)
        updater.update(file, newhash)

        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        log_entry = f"{timestamp} [UPDATED] {file} - ({oldhash} -> {newhash})\n"

        with open('logs/updater.log', 'a') as updatelog:
            updatelog.write(log_entry)


if __name__ == '__main__':
    main()
