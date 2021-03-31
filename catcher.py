import os
import time

def mkdir(folder_name):
    if os.path.exists(folder_name):
        return
    os.mkdir(folder_name)
    return

def change_mode():
    # use shell to change adapter wlan0's  mode to monitor
    mode_switch_sh = "./change_adapter_mode.sh"
    os.system(mode_switch_sh)
    return

def catcher(duration):
    # use tcpdump to get the information of the internet
    # make a folder to restore output today
    folder_name = "outputFiles" + time.strftime("%Y%m%d", time.localtime())
    mkdir(folder_name)
    # get time string 
    current_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    cmd = "sudo timeout " + str(duration) + " tcpdump -i wlan0 -n -t -e > " + folder_name + "/" + "output" + current_time
    os.system(cmd)
    
if __name__  == "__main__":
    change_mode()
    duration = eval(input("input the duratoin: "))
    for i in range(duration//3 + 1):
        catcher(3)
