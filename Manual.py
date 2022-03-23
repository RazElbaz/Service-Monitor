import json
from datetime import datetime, timedelta
from Security import secure_file, get_hash_file
import Write_to_files

"""" ***** Manual mode *****"""
def Manual():
    #ask the user for the time he want to check the processes
    start_check = input("Type the time when you want to start checking the processes in this way: year-month-day hour:minutes:seconds\n")
    end_check = input("Type the time when you want to finish reviewing the processes in this way: year-month-day hour:minutes:seconds\n")
    new_process, nonexisten_process = load(start_check, end_check)
    new_process, nonexisten_process = update(new_process, nonexisten_process)

    p= "The new process:  "
    #there are new process:
    if len(new_process)>0:
        for process in new_process:
            p += str(new_process[process])
        p+="\n"
    else:
        p+= "There are no new processes \n"
    p+= "The nonexistence process are: \n "
    #there are new process:
    if len(nonexisten_process)>0:
        for process in nonexisten_process:
            p+=str(nonexisten_process[process])
        p+="\n"
    else:
        p+= "There are no nonexistence processes\n"
    print(p)

def update(new_process,nonexisten):
    current_new = new_process
    current_nonexisten = nonexisten
    update_nonexisten_process = {j: nonexisten[j] for j in set(current_nonexisten)-set(current_new)}
    update_new_process_dict = {j: new_process[j] for j in set(current_new)-set(current_nonexisten)}
    return update_new_process_dict, update_nonexisten_process


def load(start_check, end_check):
    #dict() -> new empty dictionary
    new_process = dict()
    nonexisten_process = dict()
    #timedelta represent the difference between two datetime objects.
    time_delta = timedelta(seconds=1)

    #The strptime() function converts the character string pointed to by buf to values which are stored in the tm structure pointed to by tm, using the format specified by format
    #syntax is:time.strptime(time_string[, format])
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
            #check the absolute value of the start time
            if abs(start_time - current) < time_delta:
                new_process = json.loads(str)
                new_process = new_process.get(str(current))
                #check the absolute value of the  end time
            if abs(end_time - current) < time_delta:
                nonexisten_process = json.loads(str)
                nonexisten_process = nonexisten_process.get( str(current) )
        #close the file
        file.close()
    return new_process, nonexisten_process
if __name__ == "__main__":
    Manual()