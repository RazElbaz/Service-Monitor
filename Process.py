import Services
import Write_to_files
import json
import threading
import time
from datetime import datetime


def time_now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class Process(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=5):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval
        self.process_dict = Services.get_dict_of_process()
        self.process_born_dict = {}
        self.process_dead_dict = {}
        self.counter = 0
        self.print = True

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True  # Demonize thread
        thread.start()  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Log list of process running in sys
            service_list = {time_now(): self.process_dict}
            service_list_log = json.dumps(service_list)
            Write_to_files.write_serviceList(service_list_log)

            # Lod difference between lat log
            if self.counter != 0:
                self.diff()
                statusLog_log = self.statusLog_str()
                if self.print:
                    print(statusLog_log)
                Write_to_files.print_to_serviceList(statusLog_log)

            self.counter += 1
            time.sleep(self.interval)

    def update_process_dict(self):
        self.process_dict = Services.get_dict_of_process()
        return self.process_dict

    def diff(self):
        old_process_dict = self.process_dict
        new_process_dict = self.update_process_dict()

        self.process_dead_dict = {k: old_process_dict[k] for k in set(old_process_dict) - set(new_process_dict)}
        self.process_born_dict = {k: new_process_dict[k] for k in set(new_process_dict) - set(old_process_dict)}

    def statusLog_str(self):
        output = time_now() + '\n'
        output += 'New Process in system: '
        if len(self.process_born_dict) == 0:
            output += 'No new process\n'
        else:
            output += str(self.process_born_dict) + '\n'

        output += 'closed Process in system: '
        if len(self.process_dead_dict) == 0:
            output += 'No closed process\n'
        else:
            output += str(self.process_dead_dict) + '\n'
        return output

    def stop_print(self):
        self.print = False

    def resume_print(self):
        self.print = True


if __name__ == "__main__":
    example = Process()
    while True:
        # print('main')
        time.sleep(5)


"""""

import Write_to_files
import Services
import json
import threading
import time
from datetime import datetime

class ThreadingLog( object ):
    def __int__(self,interval=5):
        self.check=interval
        self.process=Services.system()
        self.new_process={}
        self.nonexistent={}
        self.print=True
        self.i=0


        thread=threading.Thread(target=self.run,args=())
        # i used the deanmon thread because the daemon thread does not block the main thread port and continues to run in the background as we need for the task
        thread.daemon=True
        thread.start()

    def run(self):
        services_running={time(): self.process}
        #The json. dumps() method allows us to convert a python object into an equivalent JSON objec
        services=json.dump(services_running)
        Write_to_files.write_serviceList(services)

        if self.i!=0:
            self.update()
            current_proces = self.current_process()
            if self.print:
                print(current_proces)
            Write_to_files.write_Status_Log(current_proces)

        self.i += 1
        time.sleep(self.check)


    def current_process(self):
        print=time()+"\n"
        print+="The new process in the system:  "
        #there are new process:
        if len(self.new_process)!=0:
            print+=str(self.new_process)
            print+="\n"
        else:
            print+="There are no new processes in the system"
        print+="The nonexistence process in the system:  "
        #there are new process:
        if len(self.nonexistent)!=0:
            print+=str(self.new_process)
            print+="\n"
        else:
            print+="There are no nonexistence processes in the system"
        return print

    def update(self):
        old_process_dict = self.process_dict
        new_process_dict = self.update_process()
        self.new_process = {j: new_process_dict[j] for j in set(new_process_dict) - set(old_process_dict)}
        self.nonexistent = {j: old_process_dict[j] for j in set(old_process_dict) - set(new_process_dict)}

    def update_process(self):
        self.process = Services.get_dict_of_process()
        return self.process

    def _stop(self):
        self.print = False

    def _continue(self):
        self.print = True


def time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    example = ThreadingLog()
    while True:
        # print('main')
        time.sleep(5)
"""