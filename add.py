#!/usr/bin/env python3

from db_utils import DBManager
from hash_it import hash_the_file
from datetime import datetime
from pathlib import Path
import argparse

def main():
    parser = argparse.ArgumentParser(description="Add files to the integrity checker database.")
    parser.add_argument("filepaths", type=str, help="Comma-separated list of file paths to add.")
    args = parser.parse_args()
    file_list = [file.strip() for file in args.filepaths.split(",") if file.strip()]  # Remove empty entries

    if not file_list:
        print("No valid file paths provided.")
        return

    adder = DBManager()
    log_message = 'ADDED'

    for file in file_list:
        if not Path(file).exists():
            log_message = 'DOESN\'t EXIST'
            log_action(log_message, file)
            print(f'{file} doesn\'t exists. Proceeding with other files.')
        else:
            filehash = hash_the_file(file)
            log_message = adder.add(file, filehash)
            log_action(log_message, file, filehash)


def log_action(action, file, filehash=None):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    filehash_part = f" - {filehash}" if filehash else ""
    log_entry = f"{timestamp} [{action}] {file}{filehash_part}\n"

    with open("logs/adder.log", "a") as addlog:
        addlog.write(log_entry)


if __name__ == '__main__':
    main()
