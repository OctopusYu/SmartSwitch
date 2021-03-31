import os
state = {}

def get_state(duration):
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
    print(mac_dict.keys())
    state_key = (package_count, len(mac_dict.keys()), average_rssi)
    state[state_key] = [0, 0]

if __name__ == "__main__":
    for i in range(5):
        get_state(3)
    for item in state:
        print(item)

