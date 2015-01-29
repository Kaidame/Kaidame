from __future__ import with_statement

__author__ = 'Dorbian'
__product__ = 'Kaidame'
__version__ = '0.0.1'

# Imports from the module itself
import Core.Regular_Functions as RF
import Core.logger as Logger
import Core.Arguments as Arguments
import copy
import sys
import os
import threading
import Modules.Collect
import Modules.Download
import datetime

########################
# DEVMODE SWITCH
########################
developmentmode = True
########################

# Predefine namespaces
# ------------------------------------------------------------------
# Boolean statements
__initialized__ = update = setup_completed = False
# Empty string statements
configfile = rundir = logdir = datadir = dbasefile = dbfunc = server_port = server_user = server_root = server_host = \
    server_pass = server_style = debugging = tracing = moduledir = cachedir = ''
# Empty lists
options = args = process = []
# Empty dicts
tmpd = modules = dict()
thread_lock = threading.Lock()
threading.currentThread().name = __product__
# ------------------------------------------------------------------
try:
    if not logwriter in globals():
        pass
except NameError:
    rund = RF.get_rundir()
    logwriter = Logger.Loch(rund)
    if developmentmode is True:
        logwriter._debug = True
        logwriter._trace = True
    logwriter.initialize()


def log(msg, inf):
    logwriter.log(msg, inf)


def initialize():
    with thread_lock:
        # Set all variables needed as global variables
        global __initialized__, debugging, rundir, options, args, datadir, logdir, dbasefile, configfile, dbfunc, \
            tracing, process, __product__, __version__, logwriter, webserver, cherrypy, config, cfg, \
            server_port, server_user, server_root, server_host, server_pass, server_style, DataBase, developmentmode, \
            moduledir, logwriter, cachedir, scheduler, modules, setup_completed

        # check if arguments where passed
        # ------------------------------------------------------------------
        Arguments.optsargs()

        # If set to true a lot more logging will happen
        # ------------------------------------------------------------------
        # TODO setup a seperate webserver for development mode purposes
        developmentmode = developmentmode

        # Set some statics
        # ------------------------------------------------------------------
        __version__ = __version__
        __product__ = __product__

        # Add rundirs for libs to work
        # ------------------------------------------------------------------
        rundir = RF.get_rundir()
        RF.add_rundirs(rundir)

        log("Initializing {0} {1}".format(__product__, __version__), "INFO")

        datadir = os.path.join(rundir, 'UserData')
        logdir = os.path.join(datadir, 'Logs')
        moduledir = os.path.join(rundir, os.path.join('kaidame', 'Modules'))
        cachedir = os.path.join(rundir, os.path.join('kaidame', 'Cache'))

        configfile = os.path.join(datadir, '{0}.ini'.format(__product__))
        dbasefile = os.path.join(datadir, '{0}.vdb'.format(__product__))

        RF.check_dir(datadir)
        RF.check_dir(cachedir)

        # Load scheduler
        # ------------------------------------------------------------------
        from apscheduler.scheduler import Scheduler
        scheduler = Scheduler()

        # Configuration
        # ------------------------------------------------------------------
        import Core.Conf as Config
        cfg = Config.ConfigCheck()

        # Find dynamic modules fist, then define the rest.
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

        cfg.CheckSec('General')
        setup_completed = cfg.check_bool('General', 'Setup_Complete', "False")

        cfg.config_write()

        # Initialize the database
        # ------------------------------------------------------------------
        log("Connecting to database {0}".format(dbasefile), "INFO")
        import Core.Database as Database

        # Scheduler start
        # ------------------------------------------------------------------
        scheduler.start()

        # Initialized
        # ------------------------------------------------------------------
        __initialized__ = True
        return True


def start():
    for key in modules:
        tmpt = 'import Modules.{1}.{0} as {0}'.format(key, modules[key]['Section'])
        exec tmpt
        if modules[key]['Section'] == 'Collect':
            starttime = datetime.datetime.now()
            tmpt = 'schedulet = int(Modules.{0}.{1}.SCHEDULE)'.format(modules[key]['Section'], key)
            tmps = 'scheduler.add_interval_job(Modules.{1}.{0}.start, minutes=schedulet, start_date=starttime+datetime.timedelta(minutes=1))'.format(key, modules[key]['Section'])
            exec tmpt
            exec tmps
            log("Loaded Module: {0}".format(key), "INFO")
    for job in scheduler.get_jobs():
        print job
    # try:
    #     return sys.modules['Modules.Anime.anidb']
    # except KeyError:
    #     print "Nope"
    # for key in modules:
    #
    #     exec tmps
    # for job in scheduler.get_jobs():
    #     print job


def add_names(varname, conts):
    with thread_lock:
        tmpvars = "{0} = ''".format(varname)
        tmpglob = 'global {0}'.format(varname)
        tmpcont = '{0} = {1}'.format(varname, conts)
        exec tmpvars
        exec tmpglob
        exec tmpcont



    #schedulet = int(anidb.SCHEDULE)
    #scheduler.add_interval_job(anidb.start, minutes=schedulet, start_date=starttime+datetime.timedelta(minutes=1))