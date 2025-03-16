#!/usr/bin/env python3

from pathlib import Path
import sqlite3

Path("db").mkdir(parents=True, exist_ok=True)
Path("logs").mkdir(parents=True, exist_ok=True)

Path("db/file_integrity_checker.db").touch()
Path("logs/checker.log").touch()
Path("logs/adder.log").touch()
Path("logs/remover.log").touch()
Path("logs/updater.log").touch()


connection = sqlite3.connect('file_integrity_checker.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS file_hashes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_path TEXT UNIQUE NOT NULL,
    hash_value TEXT NOT NULL,
    last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

connection.commit()
connection.close()
