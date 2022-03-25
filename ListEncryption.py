import hashlib

def secure_file(file):
    #The MD5 is a hash algorithm to turn inputs into a fixed 128-bit (16 bytes) length of the hash value
    hash=hashlib.md5()
    #open the file as "rb" mode opens the file in binary format for reading
    with open(file, "rb") as read:
        read_file=read.read()
        hash.update(read_file)
    read.close()

    return hash.hexdigest()

def get_hash_file(file, hash_file):
    return secure_file(file)==hash_file


