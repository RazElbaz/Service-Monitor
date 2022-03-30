import json
from datetime import datetime, timedelta
from Write_to_files import secure_file, get_hash_file
import Write_to_files


def Manual():
    # ask the user for the time he want to check the processes
    start_check = input(
        "Type the time when you want to start checking the processes in this way: year-month-day hour:minutes:seconds\n")
    end_check = input(
        "Type the time when you want to finish reviewing the processes in this way: year-month-day "
        "hour:minutes:seconds\n")

    Transfer_to_Jason(start_check, end_check)


def Transfer_to_Jason(start_check, end_check):
    """
    In this function we would like to use the serviceList file in order to load 2 samples from different time
    frames and make a comparison. The program will get a date and time for 2 events, load the 2 samples from the file,
    and display changes similar to the monitor mode
    """
    # dict() -> new empty dictionary
    new_process = dict()
    nonexistent_process = dict()
    # timedelta represent the difference between two datetime objects.
    time_delta = timedelta(seconds=1)

    # The strptime() function converts the character string pointed to by buf to values which are stored in the tm
    # structure pointed to by tm, using the format specified by format syntax is:time.strptime(time_string[, format])
    start_time = datetime.strptime(start_check, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(end_check, '%Y-%m-%d %H:%M:%S')
    try:
        get_hash_file('TXT_files/serviceList.txt', Write_to_files.serviceList)
    except ValueError:
        print("ERROR")
    with open('TXT_files/serviceList.txt', 'r') as file:
        flag1 = 0
        flag2 = 0
        for str in file:
            # str[2:21]-> This position in the string has the date and time
            current = datetime.strptime(str[2:21], '%Y-%m-%d %H:%M:%S')
            # check the absolute value of the start time
            if abs(start_time - current) < time_delta and flag1 != 1:
                print("The new process:  ")
                new_process = json.loads(str)
                print(new_process)
                flag1 = 1

                # check the absolute value of the  end time
            if abs(end_time - current) < time_delta and flag2 != 1:
                print("The nonexistent process:  ")
                nonexistent_process = json.loads(str)
                print(nonexistent_process)
                flag2 = 1
    # The flags were designed to ensure that only the 2 most accurate samples were taken
    if flag1 == 0:
        print("There is no new process ")
    if flag2 == 0:
        print("There is no nonexistent process")

        # close the file
        file.close()
    return new_process, nonexistent_process
