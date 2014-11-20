import kaidame
from kaidame import *
from kaidame.Core import *
import sqlite3


class dbmod():

    def __init__(self):
        self.dbfile = kaidame.dbasefile
        Logger.log("Starting up Database", "INFO")
        self.conn = None
        self.c = None

    def connect(self):
        if not os.path.exists(self.dbfile):
            Logger.log("Creating Database file", "INFO")
            self.conn = sqlite3.connect(self.dbfile)
            self.c = self.conn.cursor()
            self.setup()
        Logger.log("Connecting to Database", "INFO")
        self.conn = sqlite3.connect(self.dbfile, check_same_thread=False)
        self.c = self.conn.cursor()

    def setup(self):
        self.connect()
        try:
            self.c.execute('CREATE TABLE version(versionID TEXT UNIQUE, versionNR TEXT)')
            Logger.log("Setting up version information", "DEBUG")
        except sqlite3.OperationalError:
            try:
                self.c.execute("INSERT INTO version VALUES('1',{0})".format(kaidame.__version__))
            except:
                Logger.log("Unknown error with Database, please contact us!", "CRITICAL")
        finally:
            self.c.execute("SELECT * FROM version WHERE versionID=?", '1')
