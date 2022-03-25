import os
from os import path
from ListEncryption import secure_file, get_hash_file

serviceList = secure_file('TXT_files/serviceList.txt')
statusLog = secure_file('TXT_files/statusLog.txt')



def write_Status_Log(file, Add_to_file):
    if not path.exists(file):
        # Python code to illustrate append() mode
        with open(file, "a") as write:
            write.write(Add_to_file + "\n")
        write.close()

    #bak" is a filename extension commonly used to signify a backup copy of a file
    current = file + '.bak'
    #open the file we received in read mode and the temporary file in write mode
    with open(file, 'r') as read, open(current,"w") as write:
        write.write(Add_to_file+"\n")
        #reading from the file and writing what we read to the current file
        for s in read:
            write.write(s)

    # The OS module in Python provides functions for creating and removing a directory (folder),
    # fetching its contents, changing and identifying the current directory
    os.remove(file)

    #i changed the name of the temporary file to the name of the current file
    os.rename(current, file)
    #close the files
    read.close(),  write.close()


def write_serviceList(Add_to_file):
    file_path = 'TXT_files/serviceList.txt'
    try:
        get_hash_file(file_path,serviceList)
        write_Status_Log(file_path, Add_to_file)
        update()
    except ValueError:
        print("EROR")

def write_statusLog(Add_to_file):
    file_path = 'TXT_files/statusLog.txt'
    try:
        get_hash_file(file_path, statusLog)
        write_Status_Log(file_path, Add_to_file)
        update()
    except ValueError:
        print("EROR")

def update():
    global serviceList
    global statusLog
    serviceList = secure_file('TXT_files/serviceList.txt')
    statusLog = secure_file('TXT_files/statusLog.txt')






