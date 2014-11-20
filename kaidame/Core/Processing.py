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



def processing(targ, argse, joins, namel):
    p = Process(target=targ, args=argse, name=namel)
    p.start()
    if joins:
        p.join()