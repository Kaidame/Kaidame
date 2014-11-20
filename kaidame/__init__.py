from __future__ import with_statement

__author__ = 'Dorbian'
__product__ = 'Kaidame'
__version__ = '0.0.1'

#Imports from the module itself
from Lib import *
from Core import *

#global imports
import threading

threading.Thread.name = __product__
threadlock = threading.Lock()
#True False statements
__initialized__ = debugging = update = tracing = False
#Empty string statements
configfile = rundir = logdir = datadir = dbasefile = dbfunc = logwriter = ''
#Empty lists
options = args = threads = []
#Empty dicts
tmpd = dict()


def initialize():
    threadlock.acquire()
    #Set all variables needed as global variables
    global __initialized__, debugging, rundir, options, args, datadir, logdir, dbasefile, configfile, dbfunc, \
        tracing, logwriter, threads

    #add to the sys path for convenience
    rundir = get_rundir()
    sys.path.insert(0, rundir)

    log = Core.log

    log("Initializing {0} {1}".format(__product__, __version__), "INFO")

    #Set some directories
    datadir = os.path.join(rundir, 'Data')
    logdir = os.path.join(datadir, 'Logs')

    threads = []

    #Set some files
    configfile = os.path.join(datadir, 'config.ini')
    dbasefile = os.path.join(datadir, 'Kaidame.sqlite')

    logwriter = logwriter
    dbfunc = dbmod()

    #check if arguments where passed
    optsargs()

    debugging = True
    tracing = True

    Logger._debug = debugging
    Logger._trace = tracing

    __initialized__ = True
    threadlock.release()
    return True


def start():
    if __initialized__:
        log("Connecting to database 1", "INFO")
        dbfunc.connect()