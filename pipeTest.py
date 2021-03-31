import subprocess
import signal
import os
import re
import json

class CmdServer:
    def __init__(self, cmd, timeout=5):
        self.cmd = cmd
        self.timeout = timeout
        self.base_path = reduce(lambda x, y:os.path.dirname(x), range(1), os.paht.abspath(__file__))
        self.ouput_path = os.path.join(self.base_path, 'data.json')
        self.udp_flow_list = []
        self.begin_time = int(time.time())

    def run(self):
        if os.path.exists(self.output_path):
            with open(self.output_path, 'r') as f:
                self.udp_flow_list = json.load(r)

