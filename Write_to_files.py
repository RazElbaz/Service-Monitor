import os
from os import path

from Security import secure_file, get_hash_file

serviceList = secure_file('TXT_files/serviceList.txt')
statusLog = secure_file('TXT_files/statusLog.txt')

def update_hash():
    global serviceList
    global statusLog
    serviceList = secure_file('TXT_files/serviceList.txt')
    statusLog = secure_file('TXT_files/statusLog.txt')

def print_to_serviceList(line):
    file_path = 'TXT_files/serviceList.txt'
    if get_hash_file(file_path,serviceList):
        write_Status_Log(file_path, line)
        update_hash()
    else:
        raise ValueError('Log file' + file_path + 'was touched')

def write_serviceList(line):
    file_path = 'TXT_files/serviceList.txt'
    try:
        get_hash_file(file_path, serviceList)
        write_Status_Log(file_path, line)
        update_hash()
    except ValueError:
        print("EROR")

def write_Status_Log(file, str):
    if not path.exists(file):
        # Python code to illustrate append() mode
        with open(file, "a") as write:
            write.write(str + "\n")
        write.close()

    #bak" is a filename extension commonly used to signify a backup copy of a file
    current = file + '.bak'
    #open the file we received in read mode and the temporary file in write mode
    with open(file, "r") as read, open(current,"w") as write:
        write.write(str+"\n")
        #reading from the file and writing what we read to the current file
        for s in read:
            write.write(s)

    # The OS module in Python provides functions for creating and removing a directory (folder),
    # fetching its contents, changing and identifying the current directory

    os.remove(file)

    #We changed the name of the temporary file to the name of the current file
    os.rename(current, file)
    write.close()
    read.close()


