#!/usr/bin/env python3

from datetime import datetime
from db_utils import DBManager
from hash_it import hash_the_file
import argparse

def main():
    parser = argparse.ArgumentParser(description="Update files in the integrity checker database.")
    parser.add_argument("filepaths", type=str, help="Comma-separated list of file paths to update.")
    args = parser.parse_args()
    file_list = [file.strip() for file in args.filepaths.split(",") if file.strip()]  # Remove empty entries


    if not file_list:
        print("No valid file paths provided.")
        return

    updater = DBManager()
    for file in file_list:
        is_updated, oldhash, newhash = updater.update(file, hash_the_file(file))


        if is_updated:
            log_action('UPDATED', file, oldhash, newhash)
        else:
            log_action('ADDED', file, newhash=newhash)


def log_action(action, file, oldhash=None, newhash=None):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log_entry = f"{timestamp} [{action}] {file} - ({oldhash if oldhash else 'NONE'} -> {newhash if newhash else 'NONE'})\n"

    with open("logs/updater.log", "a") as updatelog:
        updatelog.write(log_entry)


if __name__ == '__main__':
    main()
