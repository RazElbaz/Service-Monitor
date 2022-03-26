import json
from datetime import datetime, timedelta
from Write_to_files import secure_file, get_hash_file
import Write_to_files

"""" ***** Manual mode *****"""
def Manual():
    #ask the user for the time he want to check the processes
    start_check = input("Type the time when you want to start checking the processes in this way: year-month-day hour:minutes:seconds\n")
    end_check = input("Type the time when you want to finish reviewing the processes in this way: year-month-day hour:minutes:seconds\n")
    new_process, nonexisten_process = Transfer_to_Jason(start_check, end_check)
    update(new_process, nonexisten_process)



def update(new_process,nonexisten):
    update_new={}
    update_nonexisten={}
    try:
        update_new = {j: nonexisten[j] for j in set(nonexisten)-set(new_process)}
        update_nonexisten = {j: new_process[j] for j in set(new_process)-set(nonexisten)}
    except:
        pass
    return update_nonexisten, update_new

def Transfer_to_Jason(start_check, end_check):
    #dict() -> new empty dictionary
    new_process = dict()
    nonexisten_process = dict()
    #timedelta represent the difference between two datetime objects.
    time_delta = timedelta(seconds=0.5)

    #The strptime() function converts the character string pointed to by buf to values which are stored in the tm structure pointed to by tm, using the format specified by format
    #syntax is:time.strptime(time_string[, format])
    start_time = datetime.strptime(start_check, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(end_check, '%Y-%m-%d %H:%M:%S')
    try:
        get_hash_file('TXT_files/serviceList.txt', Write_to_files.serviceList)
    except ValueError:
        print("EROR")
    with open('TXT_files/serviceList.txt', 'r') as file:
        flag1 = 0
        flag2 = 0
        for str in file:

            #str[2:21]-> This position in the string has the date and time
            current = datetime.strptime(str[2:21], '%Y-%m-%d %H:%M:%S')
            #check the absolute value of the start time
            if abs(start_time - current) < time_delta and flag1 != 1:
                print("The new process:  ")
                new_process = json.loads(str)
                print(new_process)
                flag1=1

                #check the absolute value of the  end time
            if abs(end_time - current) < time_delta and flag2 != 1:
                print("The nonexisten process:  ")
                nonexisten_process = json.loads(str)
                print(nonexisten_process)
                flag2 = 1

    if flag1==0:
        print("There is no new process")
    if flag2 == 0:
        print("There is no nonexisten process")


        #close the file
        file.close()
    return new_process, nonexisten_process


"""""""""

def Transfer_to_Jason(start_check, end_check):
    #dict() -> new empty dictionary
    new_process = dict()
    nonexisten_process = dict()
    start_time = datetime.strptime(start_check, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(end_check, '%Y-%m-%d %H:%M:%S')
    try:
        get_hash_file('TXT_files/serviceList.txt', Write_to_files.serviceList)
    except ValueError:
        print("EROR")
    with open('TXT_files/serviceList.txt', 'r') as file:
        for str in file:
            #str[2:21]-> This position in the string has the date and time
            current = datetime.strptime(str[2:21], '%Y-%m-%d %H:%M:%S')
            new_process = json.loads(str)
            new_process = new_process.get(current)
            print(new_process)
            nonexisten_process = json.loads(str)
            nonexisten_process = nonexisten_process.get(current)
        #close the file
        file.close()
    return new_process, nonexisten_process

def Transfer_to_Jason(start_check, end_check):
    #dict() -> new empty dictionary
    new_process = dict()
    nonexisten_process = dict()
    start_time = datetime.strptime(start_check, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(end_check, '%Y-%m-%d %H:%M:%S')
    try:
        get_hash_file('TXT_files/statusLog.txt', Write_to_files.serviceList)
    except ValueError:
        print("EROR")
    dictionay=dict()
    with open('TXT_files/statusLog.txt', 'r') as file:
        for str in file:
            dictionay=str.split(' ')
            #print(dictionay)
            string=" ".join(dictionay[:2])
            if string>=start_time and string<=end_time:
                new_process.append(str)

        #close the file
        file.close()
    return new_process, nonexisten_process
"""