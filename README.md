# Monitor
Service Monitor programming task

# Writing language:
Python 3.8/3.9

# Introduction:
This task opens up a tool that monitors the services(services) that run the system, and reports on changes that can be critical as SOC people.
Similar to the Zenos tool we knew - which monitors our services.

## Planning of the main departments:

**main** In this class we will pick up from the sun the mode of the monitor he chooses.

**Manual**In this class the mode is implemented manually - in this mode we would like to use the serviceList file in order to load 2 samples from different time frames and make a comparison.
The program will get a date and time for 2 events, load the 2 samples from the file and display changes similar to the monitor mode.

**Mointor** In this class a monitor mode is implemented - for X time that the user sets, the program samples every X time all the services running on the computer, and shows whether a change is observed from the previous sample. That is, is there a service that is no longer running, or is there a service
A new one is running in the system. Any change that has taken place should alert the user to the interface.

**Services** In this class, prints were made to the menu screen in the terminal, the functions for writing files were called and the list of running and non processes was updated.

**Process** In this class I checked the operating system of the same computer that our monitor runs on Linux / Windows operating systems. In addition, in this class the dictionaries for the processes were created in the following format for each process:
process pid: process name

**Write_to_files**
In this function the file was written to:
serviceList - For this file we will print the samples of the services that are currently running (each time the last sample). Each time this file will be filled in each of our samples, and will keep all the samples we made during monitor mode by date and time.
StatusLog.txt - This log file is for tracking purposes. We will print to the file any change that was shown to us in the monitor mode. For example, a new service created, a service that has stopped working, etc. In other words: everything printed to the user interface in the terminal in monitor mode will be printed to this log.

In addition, we encrypted the list of processes for security.

##  Run:
Access the main.py function and run it
Then, the menu of the instructions will open in the terminal:
   * Press 1 for Monitor mode
   * Press 2 for Manual mode
You can click 0 whenever you want to finish the program

Insert one of the above inputs as you wish
