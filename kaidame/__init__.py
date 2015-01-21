from __future__ import with_statement

__author__ = 'Dorbian'
__product__ = 'Kaidame'
__version__ = '0.0.1'

#Imports from the module itself
import Core.Logger as Logger
import Core.Regular_Functions as Regular_Functions
import Core.Database as Database
import Core.Arguments as Arguments
import copy
import sys
import os

########################
#DEVMODE SWITCH
########################
developmentmode = True
########################

#global imports
#import Processing

#Processing = Processing.Processing()
#Processing.name = __product__
#True False statements
__initialized__ = update = False
#Empty string statements
configfile = rundir = logdir = datadir = dbasefile = dbfunc = server_port = server_user = server_root = server_host = \
    server_pass = server_style = debugging = tracing = moduledir = ''
#Empty lists
options = args = process = []
#Empty functions
#Empty dicts
tmpd = dict()

try:
    if not logwriter in globals():
        pass
except NameError:
    logwriter = Logger.Loch()
    if developmentmode is True:
        logwriter._debug = True
        logwriter._trace = True
    logwriter.initialize()

def log(msg, inf):
    logwriter.log(msg, inf)

def initialize():

    #Set all variables needed as global variables
    global __initialized__, debugging, rundir, options, args, datadir, logdir, dbasefile, configfile, dbfunc, \
        tracing, process, __product__, __version__, logwriter, webserver, cherrypy, config, cfg, \
        server_port, server_user, server_root, server_host, server_pass, server_style, DataBase, developmentmode, \
        moduledir, logwriter

    #check if arguments where passed
    Arguments.optsargs()

    #If set to true a lot more logging will happen
    #TODO setup a seperate webserver for development mode purposes
    developmentmode = developmentmode

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
    moduledir = os.path.join(rundir, os.path.join('kaidame', 'Modules'))

    #Set some files
    configfile = os.path.join(datadir, '{0}.ini'.format(__product__))
    dbasefile = os.path.join(datadir, '{0}.vdb'.format(__product__))

    #Configuration
    import Core.Conf as Config
    cfg = Config.ConfigCheck()
    cfg.find_module()

    cfg.CheckSec('Server')
    server_host = cfg.check_str('Server', 'IP', '0.0.0.0')
    server_port = cfg.check_int('Server', 'Port', 7000)
    server_user = cfg.check_str('Server', 'Username', '')
    server_pass = cfg.check_str('Server', 'Password', '')
    server_root = cfg.check_str('Server', 'Webroot', '/')
    server_style = cfg.check_str('Server', 'Style', 'default')

    cfg.CheckSec('Data')
    DataBase = cfg.check_str('Data', 'Database', 'Kaidame.vdb')


    #cfg.config_validate()
    cfg.config_write()

    #Initialize the database
    dbfunc = Database.dbmod()

    log("Connecting to database {0}".format(dbasefile), "INFO")
    dbfunc.connect()

    __initialized__ = True
    return True