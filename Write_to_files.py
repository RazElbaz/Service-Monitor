import hashlib
import os
from os import path

"""""""""
The purpose of the two next functions is to encrypt the list of processes in order to be protected
"""""


def secure_file(file):
    #The MD5 is a hash algorithm to turn inputs into a fixed 128-bit (16 bytes) length of the hash value
    hash = hashlib.md5()
    with open(file, "rb") as read:
        read_file=read.read()
        hash.update(read_file)
    read.close()

    return hash.hexdigest()


def get_hash_file(file, hash_file):
    return secure_file(file)==hash_file


# create two global variables that will save the encrypted files
statusLog = secure_file('TXT_files/statusLog.txt')
serviceList = secure_file('TXT_files/serviceList.txt')


def write_Status_Log(file, Add_to_file):
    if not path.exists(file):
        # Python code to illustrate append() mode
        with open(file, "a") as write:
            write.write(Add_to_file + "\n")
        write.close()

    # "bak" is a filename extension commonly used to signify a backup copy of a file
    current = file + '.bak'
    # open the file we received in read mode and the temporary file in write mode
    with open(file, 'r') as read, open(current,"w") as write:
        write.write(Add_to_file+"\n")
        #reading from the file and writing what we read to the current file
        for s in read:
            write.write(s)

    # The OS module in Python provides functions for creating and removing a directory (folder),
    # fetching its contents, changing and identifying the current directory
    os.remove(file)

    # change the name of the temporary file to the name of the current file
    os.rename(current, file)
    read.close(),  write.close()


def write_serviceList(Add_to_file):
    file_path = 'TXT_files/serviceList.txt'
    try:
        get_hash_file(file_path,serviceList)
        write_Status_Log(file_path, Add_to_file)
    except ValueError:
        print("EROR")

def write_statusLog(Add_to_file):
    file_path = 'TXT_files/statusLog.txt'
    try:
        get_hash_file(file_path, statusLog)
        write_Status_Log(file_path, Add_to_file)
    except ValueError:
        print("EROR")





