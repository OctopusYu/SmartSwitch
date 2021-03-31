import os
import time
import subprocess
import signal
cmd = ['sudo', 'tcpdump', '-i', 'wlan0']
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
        proc.send_signal(signal.SIGINT)
        # stdout = proc.stdout.read()
        break
    print(line)
# proc.kill()
# proc.terminate()
os.killpg(os.getpgid(proc.pid), 9)
print('here')

