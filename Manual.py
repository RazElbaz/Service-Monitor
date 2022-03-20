import json
from datetime import datetime, timedelta
from Security import secure_file, get_hash_file
import Write_to_files

"""" ***** Manual mode *****"""
def Manual():
    start = input("Enter the time when you want to start checking the processes in this way: day-month-year hour:minutes:seconds\n")
    end = input("Enter the time when you want to finish reviewing the processes in this way: day-month-year hour:minutes:seconds\n")

    new_process, nonexisten_process = load(start, end)
    new_process, nonexisten_process = update(new_process, nonexisten_process)

    print="The new process in the system:  "
    #there are new process:
    if len(new_process)!=0:
        print+=str(new_process)
        print+="\n"
    else:
        print+="There are no new processes in the system"
    print+="The nonexistence process in the system:  "
    #there are new process:
    if len(nonexisten_process)!=0:
        print+=str(nonexisten_process)
        print+="\n"
    else:
        print+="There are no nonexistence processes in the system"
    print(print)

def update(new_process,nonexisten):
    current_new = new_process
    current_nonexisten = nonexisten
    update_nonexisten_process = {k: nonexisten[k] for k in set(nonexisten) - set(current_new)}
    update_new_process_dict = {k: new_process[k] for k in set(new_process) - set(current_nonexisten)}

    return update_new_process_dict, update_nonexisten_process


def load(start, end):
    #dict() -> new empty dictionary
    new_process = dict()
    nonexisten_process = dict()
    #timedelta represent the difference between two datetime objects.
    time_delta = timedelta(seconds=1)
    start_time = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')

    file_path = 'TXT_files/serviceList.txt'
    try:
        get_hash_file(file_path, Write_to_files.serviceList)
    except ValueError:
        print("EROR")

    with open('TXT_files/serviceList.txt', 'r') as file:
        for str in file:
            current = datetime.strptime(str[2:21], '%Y-%m-%d %H:%M:%S')
            #check the absolute value of the start time
            if abs(start_time - current) < time_delta:
                new_process = json.loads(str)
                new_process = new_process.get(str(current))
                #check the absolute value of the  end time
            if abs(end_time - current) < time_delta:
                nonexisten_process = json.loads(str)
                nonexisten_process = nonexisten_process.get(str(current))
        #close the file
        file.close()
    return new_process, nonexisten_process
if __name__ == "__main__":
    Manual()