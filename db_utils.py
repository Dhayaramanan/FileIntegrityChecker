import sqlite3

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect('db/file_integrity_checker.db')
        self.cursor = self.conn.cursor()

    
    def check_if_file_exists(self, filepath):
        self.cursor.execute("SELECT 1 FROM file_hashes WHERE file_path = ?", (filepath,))
        return self.cursor.fetchone() is not None


    def add(self, filepath, filehash):
        if self.check_if_file_exists(filepath):
            print(f"File '{filepath}' already exists in the database.")
            return
    
        self.cursor.execute("""
            INSERT INTO file_hashes (file_path, hash_value) VALUES (?, ?);
        """, (filepath, filehash))
        print(f"Added '{filepath}' to the database.")
        self.conn.commit()


    def remove(self, filepath):
        if not self.check_if_file_exists(filepath):
            print(f"File '{filepath}' not found in the database. Cannot delete.")
            return

        self.cursor.execute("DELETE FROM file_hashes WHERE file_path = ?", (filepath,))
        print(f"Deleted '{filepath}' from the database.")
        self.conn.commit()


    def update(self, filepath, filehash):
        if not self.check_if_file_exists(filepath):
            print(f"File '{filepath}' not found in the database. Adding it to the database.")
            self.add(filepath, filehash)
            return

        self.cursor.execute("""
            UPDATE file_hashes SET hash_value = ? WHERE file_path = ?;
        """, (filehash, filepath))
        self.conn.commit()
        print(f"Updated hash for '{filepath}'.")


    def read(self, filepath):
        if not self.check_if_file_exists(filepath):
            print(f"File '{filepath}' not found in the database.")
            return
        
        self.cursor.execute("""
            SELECT hash_value FROM file_hashes WHERE file_path = ?;
        """,(filepath,))
        result = self.cursor.fetchone()
        return result[0] if result else None
    

    def read_all(self):
        self.cursor.execute("""
            SELECT file_path, hash_value FROM file_hashes;
        """)
        return self.cursor.fetchall()
    
    
    def close(self):
        self.conn.close()
        print("Database connection is closed.")
    

    def __del__(self):
        self.close()
