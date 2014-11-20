from __future__ import with_statement

__author__ = 'Dorbian'
__product__ = 'Kaidame'
__version__ = '0.0.1'

#Imports from the module itself
from Lib import *
from Core import *

init_lock = Threader.threading.Lock()
#True False statements
__initialized__ = debugging = update = tracing = False
#Empty string statements
configfile = rundir = logdir = datadir = dbasefile = dbfunc = logwriter = ''
#Empty lists
options = args = []
#Empty dicts
tmpd = dict()


def initialize():
    with init_lock:

        #Set all variables needed as global variables
        global __initialized__, debugging, rundir, options, args, datadir, logdir, dbasefile, configfile, dbfunc, \
            tracing, logwriter

        #add to the sys path for convenience
        rundir = get_rundir()
        sys.path.insert(0, rundir)

        log = Core.

        #Set some directories
        datadir = os.path.join(rundir, 'Data')
        logdir = os.path.join(datadir, 'Logs')

        log("Initializing {0} {1}".format(__product__, __version__), "INFO")

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
    return True


def start():
    if __initialized__:
        dbfunc.connect()