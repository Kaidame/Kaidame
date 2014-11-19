from __future__ import with_statement

__author__ = 'Dorbian'


import logger
import threader
import commandcenter
import server
import database
import os
import Lib
import Modules.Reporting
from framework.Core import Regular_Functions, reporting, Config

import sys
import time


init_lock = threader.threading.Lock()
__initialized__ = debugging = False

def initialize(state):
    if state == "BOOT":
        logger.log("Booting Framework, please wait!", "INFO")
    elif state == "REBOOT":
        logger.log("Rebooting Framework, please wait!", "INFO")

    with init_lock:

        global __initialized__, commandlist, dbfile, configfile, workingdir, templatedir, ssimserver, \
            ssimuser, ssimpwd, config, debugging, logdir, logfile, guitype, guilock, serverstart, ostype, pyver, db, \
            version

    __initialized__ = True


def start():
    global serverstart
    serverstart = server.CommandServer()
    serverstart.start()