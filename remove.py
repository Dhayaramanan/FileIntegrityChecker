#!/usr/bin/env python3

from db_utils import DBManager
from datetime import datetime
import argparse

def main():
    parser = argparse.ArgumentParser(description="remove files from the integrity checker database.")
    parser.add_argument("filepaths", type=str, help="Comma-separated list of file paths to remove.")
    args = parser.parse_args()
    file_list = [file.strip() for file in args.filepaths.split(",") if file.strip()]  # Remove empty entries

    if not file_list:
        print("No valid file paths provided.")
        return

    remover = DBManager()

    for file in file_list:
        filehash = remover.read(file)
        if not filehash:
            log_action("DOESN'T EXISTS", file)
        else:
            remover.remove(file)
            log_action('REMOVED', file, filehash)


def log_action(action, file, filehash=None):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    filehash_part = f" - {filehash}" if filehash else ""
    log_entry = f"{timestamp} [{action}] {file}{filehash_part}\n"

    with open("logs/remover.log", "a") as removelog:
        removelog.write(log_entry)


if __name__ == '__main__':
    main()
