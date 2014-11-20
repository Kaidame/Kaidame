import threading
import kaidame
from kaidame import *
from kaidame.Core import *


class Thread(threading.Thread):
    def __init__(self, threadid, name, command):
        threading.Thread.__init__(self)
        self.threadID = threadid
        self.name = name
        self.command = command

    def run(self):
        Logger.log("Starting Thread {0}".format(self.name), "INFO")
        self.command()