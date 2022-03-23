import subprocess
from builtins import print
import psutil
from platform import system

def Linux():
    output = subprocess.check_output(["service", "--status-all"])
    service_list = list()
    for line in output.split('\n'.encode(encoding='UTF-8')):
        string = str(line)
        service_name = string[10:- 1]
        service_list.append(service_name)

    service_dict = {p.pid: p.name() for p in psutil.process_iter(['name']) if p.info['name'] in service_list}
    return service_dict


def set_processes():
    process_dict = {p.pid: p.info for p in psutil.process_iter(['name'])}
    process_dict = {key: process_dict.get(key).get('name') for key in process_dict}
    return process_dict


def Windows():
    service_dict = [s for s in psutil.win_service_iter()]
    service_dict = {s.pid(): s.name() for s in service_dict}
    return service_dict


def get_process():
    Operating_System = system()
    if Operating_System == 'Windows':
        return Windows()
    elif Operating_System == 'Linux':
        return Linux()
    else:
        raise ValueError("This monitor is not supported in your system")




