import psutil
import subprocess
from platform import system

def get_pid(name):
    return subprocess.check_output(["pidof" , "-s", name]).decode()[:-1]
# def get_pid(name):
#     return [subprocess.check_output(["pidof",name]).decode().split()]



def get_process():
    Operating_System = system()
    if Operating_System == 'Windows':
        return Windows()
    elif Operating_System == 'Linux':
        return Linux()
    else:
        raise ValueError("This monitor is not supported in your system")


def set_processes():
    Processes={}
    if system() == 'Windows':
        Processes = {pid.name(): pid.info for pid in psutil.process_iter(['name'])}
        Processes = {key: psutil.win_service_get(Processes.get(key)).status() for key in Processes}

    elif system() == 'Linux':
        Process=Linux()
        print(Process)
    return Processes



def Linux():
    Process = {}
    cnt=0
    process = subprocess.check_output("service --status-all", shell=True).decode("UTF-8")
    for service in process.split('\n')[:-1]:
        curr_name = service[8:]
        status = "running" if service[3] == '+' else "stopped"
        if status == "stopped":
            pid =0
        else:
            try:
                pid = int(get_pid(curr_name))
            except:
                pid = cnt
                cnt -= 1

        Process[pid] = curr_name
    return Process
    # p1 = subprocess.run(['ls', '-la'], capture_output=True, text=True)

    # p2 = str(p1.stdout)
    # for line in p2.split('\n'):
    #     if line == "":
    #         continue
    #     string = str(line)
    #     pid = string[20:25]
    #     name = string[39:]
    #     pid_split = pid.split(' ')
    #     for ans in pid_split:
    #         if ans != '':
    #             Process[name] = int(ans)



def Windows():
    service_dict = [s for s in psutil.win_service_iter()]
    service_dict = {s.pid(): s.name() for s in service_dict}
    return service_dict



def lin_service_get_status(name):
    process = subprocess.check_output("service --status-all", shell=True).decode("UTF-8")
    for service in process.split('\n')[:-1]:
        curr_name = service[8:]
        if curr_name == name:
            return "running" if service[3] == '+' else "stopped"





