from multiprocessing import Process, Lock
#import Kaidame
#from kaidame import *
import socket, select
#https://docs.python.org/2/library/multiprocessing.html


class Proc():

    def __init__(self):
        self.p = ''
        self.lock = ''
        self.name = ''
        pass

    def start(self, targ, argse, namel, dmn=False):
        self.p = Process()
        self.p._target = targ
        self.p._args = argse
        self.p._name = namel
        if dmn:
            self.p.daemon = True
        self.p.start()

    def lock(self):
        self.lock = Lock()

    def kill(self, namel):
        self.p.join(name=namel)

<<<<<<< Updated upstream

def proces(targ, argse, joins, namel, lock=False):
=======
def process(targ, argse, joins, namel):
>>>>>>> Stashed changes
    p = Process(target=targ, args=argse, name=namel)
    if lock:
        pass
    p.start()
    if joins:
        p.join()
