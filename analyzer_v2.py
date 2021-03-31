import os
import threading
import time

states = {}
syn = 0
state_tuple = tuple()
stop_flag = False

def get_a_state(duration):
    cmd = "sudo timeout " + str(duration) + " tcpdump -i wlan0 -n -t -e > output"
    os.system(cmd)
    f = open("output", 'r', encoding = 'utf-8')
    ls_line = [line for line in f.readlines()]
    f.close()

    average_rssi = 0
    mac_dict = {}
    package_count = len(ls_line)
    sum_rssi = 0

    for item in ls_line:
        index = item.find("dBm")
        if index != -1:
            sum_rssi += int(item[index - 2:index]) 
        index = item.find("BSSID")
        if index != -1:
            mac_address = item[index + 6 : index + 24]
            mac_dict[mac_address] = mac_dict.get(mac_address, 0) + 1;

        index = item.find("RA")
        if index != -1:
            mac_address = item[index + 3 : index + 21]

        index = item.find("SA")
        if index != -1:
            mac_address = item[index + 3 : index + 21]

        index = item.find("DA")
        if index != -1:
            mac_address = item[index + 3 : index + 21]

        index = item.find("TA")
        if index != -1:
            mac_address = item[index + 3 : index + 21]

    average_rssi = sum_rssi // package_count
    state_key = (package_count, len(mac_dict.keys()), average_rssi)
    return (state_key , [0, 0])

def generate_a_state():
    while 1:
        syn = 0
        state_tuple = get_a_state(3);
        syn = 1
        time.sleep(1)
        if stop_flag:
            break

if __name__ == "__main__":
    get_state_thread = threading.Thread(target = generate_a_state, args = ())
    get_state_thread.start()
    while 1:
        print("Please input operator ( on, off, stop ):")
        op = input(">>>> ")
        if op == 'on' or op == 'off':
            while(syn == 0):
                time.sleep(0.01)
            print(state_tuple)
            states[state_tuple[0]] = state_tuple[1]
        if op == 'stop':
            stop_flag = True
            time.sleep(4)
            get_state_thread.join()
            break
    for item in states:
        print(item)
