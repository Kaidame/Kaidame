# import kaidame
# from kaidame import *
# from kaidame.Core import *
# import re
import os
import json

#Class for parsing filenames, to see what is what.
class walker():

    def __init__(self):
        self.downloaddir = '/Users/Dorbian/Movies'
        self.moviecheck = True

class moviechecker():

    def checklength(self, movfile):
        self.file = movfile
        for f in os.listdir('.'):
            print "%s: %s" % (f, getLength(f))


class parse():

    def __init__(self):
        self.input = ''

    def checkname(self, txt):
        self.input = txt
        #log("Parsing {0}".format(txt), 'INFO')

mv = moviechecker()
mv.checklength('/Users/Dorbian/Movies')