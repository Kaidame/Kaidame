import kaidame
from kaidame import *
from kaidame.Core import *
import sys
import os

#New format logging IMHO a better practice
def log(message, level):
    if str(level).lower() == 'debug':
        logwriter.log(message, lvl='DEBUG')
    elif str(level).lower() == 'info':
        logwriter.log(message, lvl='INFO')
    elif str(level).lower() == 'warning':
        logwriter.log(message, lvl='WARN')
    elif str(level).lower() == 'error':
        logwriter.log(message, lvl='ERROR')
    elif str(level).lower() == 'trace':
        logwriter.log(message, lvl='TRACE')
    else:
        logwriter.log(message, lvl='')


#Check if we are an exe made by py2exe
def check_frozen():
    return hasattr(sys, 'frozen')


#Get the directory we are running in
def get_rundir():
    if check_frozen():
        return os.path.abspath(unicode(sys.executable, sys.getfilesystemencoding()))

    return os.path.abspath(__file__)[:-34]


#Check if we need to update or not
def get_update():
    pass

def add_rundirs(rundir):
    appdir = os.path.join(rundir, "kaidame")
    sys.path.append(rundir)
    sys.path.append(appdir)
    sys.path.append(os.path.join(appdir, "Lib"))
    sys.path.append(os.path.join(os.path.join(appdir, "Lib"), "cherrypy"))


def quit():
    for t in kaidame.threads:
        t.join()
    log("Exiting main Thread", "INFO")