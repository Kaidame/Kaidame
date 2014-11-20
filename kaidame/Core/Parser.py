import kaidame
from kaidame import *
from kaidame.Core import *
import re


#Class for parsing filenames, to see what is what.
class parse():

    def __init__(self):
        self.input = ''

    def checkname(self, txt):
        self.input = txt
        log("Parsing {0}".format(txt), 'INFO')
