import Manual
import Process


"""" ***** Monitor mode *****"""
def Monitor():
    wating_time= int(input("Please insert the interval that we will update you in a new process\n"))
    thread = Process.Process(wating_time)
    print("You can click 2 whenever you want to change the monitor mode to the Manual mode\n\n")
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
            exit(0)

if __name__ == "__main__":
    Monitor()
