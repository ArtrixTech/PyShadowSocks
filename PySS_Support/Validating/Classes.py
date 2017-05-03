from PySS_Support.Classes import SSServer
import socket
import subprocess
import re

import datetime
import os


class LinkState(object):

    import time
    packetLossRate = ""
    averageTime = ""
    ip = ""

    def __init__(self, ip):
        self.ip = ip

    def ping(self):
        # 运行ping程序
        p = subprocess.Popen(["cmd.exe", "/C ping -n 2 %s" % self.ip],
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             shell=True)

        # set the timeout
        start = datetime.datetime.now()
        timeout = 4
        while p.poll() is None:
            self.time.sleep(0.2)
            now = datetime.datetime.now()
            if (now - start).seconds > timeout:
                p.terminate()
                print("Failed!")
                return False
        # 得到ping的结果
        out = bytes(p.stdout.read()).decode("gb2312")
        # print(out)
        try:
            regex = re.compile(r'\w*ms')
            time = regex.findall(out)
            return time[-1]
        except:
            return False


class ValidateTest:

    _server = SSServer()
    _host = ""

    def __init__(self, server):
        self._server = server

    def test(self):
        server = self._server
        self._server = server
        self._host = socket.gethostbyname(server.ip)
        state = LinkState(self._host).ping()
        state2 = LinkState(self._host).ping()
        if state and state2:
            return int((int(state.replace("ms",""))+int(state2.replace("ms","")))/2)
        else:
            return False
