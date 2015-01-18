from __future__ import with_statement

__author__ = 'Dorbian'
__product__ = 'Kaidame'
__version__ = '0.0.1'

#Imports from the module itself
import Core.Logger as Logger
import Core.Regular_Functions as Regular_Functions
import Core.Database as Database
import Core.Arguments as Arguments
import sys
import os

#global imports
#import Processing

#Processing = Processing.Processing()
#Processing.name = __product__
#True False statements
__initialized__ = debugging = update = tracing = False
#Empty string statements
configfile = rundir = logdir = datadir = dbasefile = dbfunc = server_port = server_user = server_root = server_host = \
    server_pass = ''
#Empty lists
options = args = process = []
#Empty functions
#Empty dicts
tmpd = dict()

try:
    if not logwriter in globals():
        pass
except NameError:
    print "log init"
    logwriter = Logger.Loch()
    logwriter.initialize()

def log(msg, inf):
    logwriter.log(msg, inf)

def initialize():

    #Set all variables needed as global variables
    global __initialized__, debugging, rundir, options, args, datadir, logdir, dbasefile, configfile, dbfunc, \
        tracing, process, __product__, __version__, logwriter, webserver, cherrypy, \
        server_port, server_user, server_root, server_host, server_pass

    #add to the sys path for convenience

    __version__ = __version__
    __product__ = __product__
    #Add rundirs for libs to work
    rundir = Regular_Functions.get_rundir()
    Regular_Functions.add_rundirs(rundir)

    log("Initializing {0} {1}".format(__product__, __version__), "INFO")

    #Set some directories
    datadir = os.path.join(rundir, 'Data')
    logdir = os.path.join(datadir, 'Logs')

    #Set some files
    configfile = os.path.join(datadir, '{0}.ini'.format(__product__))
    dbasefile = os.path.join(datadir, '{0}.vdb'.format(__product__))

    #Configuration
    import Core.Config as Config
    cfg = Config.ConfigCheck()
    cfg.config_validate()

    server_port = cfg['SERVER']['Port']
    server_user = cfg['SERVER']['Username']
    server_root = cfg['SERVER']['Webroot']
    server_host = cfg['SERVER']['IP']
    server_pass = cfg['SERVER']['Password']

    debugging = cfg['DEVELOPMENT']['Debug']
    tracing = cfg['DEVELOPMENT']['Tracing']


    #Initialize the database
    dbfunc = Database.dbmod()

    #check if arguments where passed
    Arguments.optsargs()

    #Write the config back to the system
    cfg.config_write()


    Logger.Loch._debug = debugging
    Logger.Loch._trace = tracing


    log("Connecting to database 1", "INFO")
    dbfunc.connect()

    __initialized__ = True
    return True