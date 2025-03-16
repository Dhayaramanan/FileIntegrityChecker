#!/usr/bin/env python3

from db_utils import DBManager
from datetime import datetime
import argparse

def main():
    parser = argparse.ArgumentParser(description="remove files from the integrity checker database.")
    parser.add_argument("filepaths", type=str, help="Comma-separated list of file paths to remove.")
    args = parser.parse_args()
    file_list = args.filepaths.split(",")

    remover = DBManager()

    for file in file_list:
        filehash = remover.read(file)
        remover.remove(file)
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        log_entry = f"{timestamp} [REMOVED] {file} - {filehash}\n"

        with open('logs/remover.log', 'a') as removelog:
            removelog.write(log_entry)


if __name__ == '__main__':
    main()
