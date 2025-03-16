import hashlib

def hash_the_file(filepath, algorithm='sha256'):
    hash_func = hashlib.new(algorithm)

    with open(filepath, 'rb') as file:
        while chunk := file.read(8192):
            hash_func.update(chunk)

    return hash_func.hexdigest()
