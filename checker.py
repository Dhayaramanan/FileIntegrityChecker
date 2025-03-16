#!/usr/bin/env python3

from datetime import datetime
from db_utils import DBManager
from hash_it import hash_the_file
from subprocess import run


def main():
    data = DBManager().read_all()

    for filepath, stored_hash in data:
        new_hash = hash_the_file(filepath)

        if new_hash != stored_hash:
            write_log(filepath, stored_hash, new_hash, modified=1)
            send_notification(filepath)
        else:
            write_log(filepath, stored_hash, new_hash)


def write_log(filepath, store_hash, new_hash, modified=0):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log_entry = f"{timestamp} {filepath} - {'MODIFIED' if modified else 'NOT_MODIFIED'} ({store_hash} -> {new_hash})\n"
    with open('logs/checker.log', 'a') as file:
        file.write(log_entry)


def send_notification(filepath):
    run(['notify-send', 'File Integrity Alert', f'{filepath} has been modified.'])


if __name__ == '__main__':
    main()
