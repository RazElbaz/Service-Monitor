import Manual
import Process

"""" ***** Monitor mode *****"""
def Monitor():
    Time=time()
    thread = Process.ProcessThread(Time)
    print("You can click 2 whenever you want to change the monitor mode to the Manual mode\n")
    while True:
        i = input('\n')
        #stop the moninotor mode and chande to manuel mode
        if i == '2':
            #stop the thread missiom
            thread._stop()
            #change the mood
            Manual.Manual()
            #continue the thread mission, now in manual mood
            thread._continue()

        #if the user want to get out of the program
        elif i == '0':
            print("********* Shutdown of monitor ************")
            exit(0)

def time():
    return int(input("Please insert the interval that we will update you in a new process\n"))

