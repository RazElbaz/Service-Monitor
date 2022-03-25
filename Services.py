import psutil
import subprocess
from platform import system
from builtins import print

def get_process():
    Operating_System = system()
    if Operating_System == 'Windows':
        return Windows()
    elif Operating_System == 'Linux':
        return Linux()
    else:
        raise ValueError("This monitor is not supported in your system")

def set_processes():
    Processes = {p.pid: p.info for p in psutil.process_iter(['name'])}
    Processes = {key: Processes.get(key).get('name') for key in Processes}
    return Processes


def Linux():
    Processes = subprocess.check_output(["service", "--status-all"])
    List = list()
    for line in Processes.split('\n'.encode(encoding='UTF-8')):
        string = str(line)
        process = string[10:- 1]
        List.append(process)

    Processes_list = {p.pid: p.name() for p in psutil.process_iter(['name']) if p.info['name'] in List}
    return Processes_list




def Windows():
    service_dict = [s for s in psutil.win_service_iter()]
    service_dict = {s.pid(): s.name() for s in service_dict}
    return service_dict







