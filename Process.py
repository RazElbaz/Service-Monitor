import json
import time
import Services
import threading
import Write_to_files
from datetime import datetime

class ProcessThread(object):
    def __init__(self, time_for_update=3):
        #flag for priting
        self.print = True
        self.i = 0
        #check is a variable that the user need to enter and this is the time for update the process list
        self.check=time_for_update
        self.process=Services.get_process()
        #dictionarys for the process
        self.new_process={}
        self.nonexistent={}
        #starting the thread
        thread=threading.Thread(target=self.run,args=())
        # i used the deanmon thread because the daemon thread does not block the main thread port and continues to run in the background as we need for the task
        thread.daemon=True
        thread.start()

    def run(self):
        while True:
            service_list = {datetime.now().strftime('%Y-%m-%d %H:%M:%S'): self.process}
            # The json. dumps() method allows us to convert a python object into an equivalent JSON objec
            service_list_log = json.dumps(service_list)
            Write_to_files.write_serviceList(service_list_log)

            if self.i != 0:
                self.update()
                processes = self.current_process()
                if self.print:
                    print(processes)
                Write_to_files.write_statusLog(processes)

            self.i += 1
            #i used a sleep function to slow down the print rate of the processes
            time.sleep(self.check)

    def update(self):
        current_nonexistent = self.process
        current_new_process = self.set_process()
        #The set() function creates a set in Python.
        #in order to update the new and old processes, I made a subtraction between the two lists
        self.nonexistent = {
            j: current_nonexistent[j]
            for j in set(current_nonexistent)-set(current_new_process)}
        self.new_process = {
            j: current_new_process[j]
            for j in set(current_new_process)-set(current_nonexistent)}


    def current_process(self):
        print = "**********************************************************\n"
        print+=datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\n"
        print+="The new process is:  "
        if len(self.new_process)!=0:
            print+=str(self.new_process)
            print+="\n"
        else:
            print+="---\n"
        print+="The nonexistence process is:  "
        #there are new process:
        if len(self.nonexistent)!=0:
            print+=str(self.nonexistent)
            print+="\n"
        else:
            print+="---\n"
        print+="**********************************************************\n"
        return print

    def set_process(self):
        self.process = Services.get_process()
        return self.process

    def _stop(self):
        self.print = False

    def _continue(self):
        self.print = True




