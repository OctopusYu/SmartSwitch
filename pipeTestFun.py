import os
import time
import subprocess
import signal
cmd = ['sudo', 'tcpdump', '-i', 'wlan0']
def catch():
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    begin_time = int(time.time())
    while True:
        line = proc.stdout.readline()
        line = line.strip()
        if not line:
            print('tcpdump finished...')
            break
        end_time = int(time.time())
        if end_time - begin_time >= 3:
            print('time is running out')
            # proc.send_signal(signal.SIGINT)
            proc.kill()
            # proc.terminate()
            # stdout = proc.stdout.read()
            # os.killpg(os.getpgid(proc.pid), 9)
            break
        print(line)
    # os.killpg(os.getpgid(proc.pid), 9)
print('Now want to catch the frame')
catch()
for i in range (5):
    print('here')
