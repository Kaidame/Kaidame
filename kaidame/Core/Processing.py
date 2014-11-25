from multiprocessing import Process, Lock
import Kaidame
from kaidame import *
import socket, select
#https://docs.python.org/2/library/multiprocessing.html


class Proc():

    def __init__(self):
        self.p = ''
        self.lock = ''
        self.name = ''
        pass

    def start(self, targ, argse, namel, dmn=False):
        self.p = Process(target=targ, args=argse, name=namel)
        try:
            log(self.p.name, "INFO")
        except NameError:
            pass
        if dmn:
            try:
                log('Daemonizing', "INFO")
            except NameError:
                pass
            self.p.daemon = True
        self.p.start()

    def lock(self):
        self.lock = Lock()


def proces(targ, argse, joins, namel, lock=False):
    p = Process(target=targ, args=argse, name=namel)
    if lock:
        pass
    p.start()
    if joins:
        p.join()


class CommandServer:

    def __init__(self):
        self.port = 21
        self.host = "localhost" #socket.gethostname()

        self.srvsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.srvsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.srvsock.bind((self.host, self.port))
        self.srvsock.listen(50)

        self.descriptors = [self.srvsock]
        log('Server started', "INFO")

    def start(self):
        #Create server thread
        kaidame.processing.start(self.run('Strings'), '', 'Server', dmn=True)

    def run(self, stri):
        print stri
        cont = None
        while 1:
            (sread, swrite, sexc) = select.select(self.descriptors, [], [])

            # Iterate through the tagged read descriptors
            for sock in sread:

                # Received a connect to the server (listening) socket
                if sock == self.srvsock:
                    self.accept_new_connection()
                else:
                    # Received something on a client socket
                    try:
                        str1 = sock.recv(4096)
                        cont = True
                    except:
                        host, port = sock.getpeername()
                        print('Client disconnected')
                        rows = [(port)]
                        #sock.close()
                        self.descriptors.remove(sock)
                        cont = False
                    # Check to see if the peer socket closed
                    if cont:
                        host, port = sock.getpeername()
                        newstr = '{0}:{1}//{2}'.format(host, port, str1)
                        self.receive_string(newstr)

    def receive_string(self, strs):
        str_split = strs.split('//')
        if str_split[1].startswith("IDENTIFY"):
            host = str_split[0]
            host = host.split(':')
            hostip = host[0]
            hostport = host[1]
            hosttmp = str_split[1]
            hosttmp = hosttmp.split('-::-')
            hostnode = hosttmp[0]
            hostnode = hostnode.split(':')
            hostnode = hostnode[1]
            hostos = hosttmp[1]
            hostsoft = hosttmp[2]
            rows = [(hostip, hostport, hostsoft, hostnode, hostos)]
            client = self.hostbuild(hostip, hostport)
            self.send_string('IDENTIFY:OK', client)

    def hostbuild(self, ip, port):
        host = [str(ip), int(port)]
        host = tuple(host)
        return host

    def send_string(self, strs, host):
        for sock in self.descriptors:
            if sock != self.srvsock:
                sock.sendto(strs, host)

    def broadcast_string(self, strs, omit_sock):
        for sock in self.descriptors:
            if sock != self.srvsock and sock != omit_sock:
                sock.send(strs)

    def accept_new_connection(self):
        newsock, (remhost, remport) = self.srvsock.accept()
        self.descriptors.append(newsock)

        newsock.send("Connected to the Framework v3 Server\r\n")
        print('Client connected')

    def list_connections(self):
        pass


    def send_command(self, command, host, port):
        host = [str(host), int(port)]
        host = tuple(host)
        self.broadcast_string(command, self.srvsock, host)
