import Manual
import Monitor

if __name__ == "__main__":
    print("Service Monitor")
    monitor_mode=input("**************************************\n"
                        "*********** Monitor menu: ************\n"
                       "  * Press 1 for Monitor mode\n"
                       "  * Press 2 for Manual mode\n"
                       "**************************************\n"
                       "**************************************\n"
                       "You can click 0 whenever you want to finish the program \n")
    if monitor_mode=='1':
        Monitor.Monitor()
    elif monitor_mode=='2':
        Manual.Manual()
