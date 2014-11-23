from multiprocessing import Process, Lock
#https://docs.python.org/2/library/multiprocessing.html
class processing():

    def __init__(self):
        pass

    def start(self, targ, argse, joins, namel):
        self.p = Process(target=targ, args=argse, name=namel)
        self.p.start()
        self.p.terminate()

    def lock(self):
        self.lock = Lock()


def proces(targ, argse, joins, namel, *lock):
    p = Process(target=targ, args=argse, name=namel)
    if lock:
        pass
    p.start()
    if joins:
        p.join()


def test(tst=False):
    if tst:
        print "bawls"

test()