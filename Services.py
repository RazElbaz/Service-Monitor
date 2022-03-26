import psutil
import subprocess
from platform import system


def get_process():
    Operating_System = system()
    if Operating_System == 'Windows':
        return Windows()
    elif Operating_System == 'Linux':
        return Linux()
    else:
        raise ValueError("This monitor is not supported in your system")


def set_processes():
    Processes = {p.name(): p.info for p in psutil.process_iter(['name'])}
    Processes = {key: psutil.win_service_get(Processes.get(key)).status() for key in Processes}
    return Processes


def Linux():
    p1 = subprocess.run(['ls', '-la'], capture_output=True, text=True)
    Process = {}
    p2 = str(p1.stdout)
    for line in p2.split('\n'):
        if line == "":
            continue
        string = str(line)
        pid = string[20:25]
        name = string[39:]
        pid_split = pid.split(' ')
        for ans in pid_split:
            if ans != '':
                Process[name] = int(ans)
    return Process


def Windows():
    service_dict = [s for s in psutil.win_service_iter()]
    service_dict = {s.pid(): s.name() for s in service_dict}
    return service_dict

