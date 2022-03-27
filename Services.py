import psutil
import subprocess
from platform import system


def get_pid(name):
    return subprocess.check_output(["pidof", "-s", name]).decode()[:-1]


def get_process():
    Operating_System = system()
    if Operating_System == 'Windows':
        return Windows()
    elif Operating_System == 'Linux':
        return Linux()
    else:
        raise ValueError("This monitor is not supported in your system")


def set_processes():
    Processes = {}
    if system() == 'Windows':
        Processes = Windows()
    elif system() == 'Linux':
        Process = Linux()
    return Processes


def Linux():
    Process = {}
    cnt = 0
    process = subprocess.check_output("service --status-all", shell=True).decode("UTF-8")
    for service in process.split('\n')[:-1]:
        curr_name = service[8:]
        status = "running" if service[3] == '+' else "stopped"
        if status == "running":
            Process[curr_name] = status
    return Process


def Windows():
    service_dict = [s for s in psutil.win_service_iter()]
    service_dict = {s.name(): s.status() for s in service_dict if s.status() != "stopped"}
    return service_dict


def lin_service_get_status(name):
    process = subprocess.check_output("service --status-all", shell=True).decode("UTF-8")
    for service in process.split('\n')[:-1]:
        curr_name = service[8:]
        if curr_name == name:
            return "running" if service[3] == '+' else "stopped"
