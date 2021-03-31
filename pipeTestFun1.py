import os
import time
import subprocess
import signal
cmd = ['timeout', '5', 'sudo', 'tcpdump', '-i', 'wlan0', '-n', '-t']
buf = []
def catch():
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    while True:
        line = proc.stdout.readline()
        line = line.strip()
        if not line:
            # print('tcpdump finished...')
            proc.kill()
            break
        buf.append(line)
        # print(line)

catch()
print(len(buf))
for line in buf:
    index = line.find('dBm')
    print(line[index-2:index])
    # print(line)
