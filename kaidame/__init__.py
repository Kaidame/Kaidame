from __future__ import with_statement

__author__ = 'Dorbian'
__product__ = 'Kaidame'
__version__ = '0.0.1'

#Imports from the module itself
import Core.Logger as Logger
import Core.Regular_Functions as Regular_Functions
import Core.Arguments as Arguments
import copy
import sys
import os
import threading
import datetime

########################
#DEVMODE SWITCH
########################
developmentmode = True
########################

#Predefine namespaces
#------------------------------------------------------------------
#Boolean statements
__initialized__ = update = False
#Empty string statements
configfile = rundir = logdir = datadir = dbasefile = dbfunc = server_port = server_user = server_root = server_host = \
    server_pass = server_style = debugging = tracing = moduledir = cachedir = ''
#Empty lists
options = args = process = []
#Empty dicts
tmpd = modules = dict()
thread_lock = threading.Lock()
#------------------------------------------------------------------
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
    with thread_lock:
        #Set all variables needed as global variables
        global __initialized__, debugging, rundir, options, args, datadir, logdir, dbasefile, configfile, dbfunc, \
            tracing, process, __product__, __version__, logwriter, webserver, cherrypy, config, cfg, \
            server_port, server_user, server_root, server_host, server_pass, server_style, DataBase, developmentmode, \
            moduledir, logwriter, cachedir, scheduler, modules

        #check if arguments where passed
        #------------------------------------------------------------------
        Arguments.optsargs()

        #If set to true a lot more logging will happen
        #------------------------------------------------------------------
        #TODO setup a seperate webserver for development mode purposes
        developmentmode = developmentmode

        #Set some statics
        #------------------------------------------------------------------
        __version__ = __version__
        __product__ = __product__

        #Add rundirs for libs to work
        #------------------------------------------------------------------
        rundir = Regular_Functions.get_rundir()
        Regular_Functions.add_rundirs(rundir)

        log("Initializing {0} {1}".format(__product__, __version__), "INFO")

        datadir = os.path.join(rundir, 'Data')
        logdir = os.path.join(datadir, 'Logs')
        moduledir = os.path.join(rundir, os.path.join('kaidame', 'Modules'))
        cachedir = os.path.join(rundir, os.path.join('kaidame', 'Cache'))

        configfile = os.path.join(datadir, '{0}.ini'.format(__product__))
        dbasefile = os.path.join(datadir, '{0}.vdb'.format(__product__))

        #Load scheduler
        #------------------------------------------------------------------
        from apscheduler.scheduler import Scheduler
        scheduler = Scheduler()


        #Configuration
        #------------------------------------------------------------------
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

        cfg.config_write()

        #Import modules
        #------------------------------------------------------------------
        for key in modules:
            tmp = 'import Modules.{1} as {0}'.format(key, modules[key])
            exec tmp
            log('Imported {0} from Modules.{1}'.format(key, modules[key]), 'DEBUG')

        #Initialize the database
        #------------------------------------------------------------------
        log("Connecting to database {0}".format(dbasefile), "INFO")
        import Core.Database as Database

        #Scheduler start
        #------------------------------------------------------------------
        scheduler.start()

        #Initialized
        #------------------------------------------------------------------
        __initialized__ = True
        return True


def start():
    try:
        return sys.modules['Modules.Anime.anidb']
    except KeyError:
        print "Nope"
    for key in modules:
        tmpt = 'schedulet = int(Anime.{0}.SCHEDULE)'.format(key)
        exec tmpt
        tmps = 'scheduler.add_interval_job(Anime.{0}.start, minutes=schedulet, start_date=starttime+datetime.timedelta(minutes=1))'.format(key)
        exec tmps
    for job in scheduler.get_jobs():
        print job


def add_module(varname, conts):
    with thread_lock:
        tmpvars = "{0} = ''".format(varname)
        tmpglob = 'global {0}'.format(varname)
        tmpcont = '{0} = {1}'.format(varname, conts)
        exec tmpvars
        exec tmpglob
        exec tmpcont



    #schedulet = int(anidb.SCHEDULE)
    #scheduler.add_interval_job(anidb.start, minutes=schedulet, start_date=starttime+datetime.timedelta(minutes=1))