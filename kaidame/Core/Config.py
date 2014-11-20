import kaidame
from kaidame import *
from kaidame.Core import *
from kaidame.Lib import *


class ConfigCheck():

    def __init__(self):
        self.configfile = kaidame.configfile
        self.config = None
        self.results = None
        self.validator = Validator()

    def config_validate(self):
        try:
            self.config = ConfigObj(configspec='./framework/Core/configspec.ini', file_error=True)
            self.config.filename = self.configfile
        except (ConfigObjError, IOError), e:
            Logger.log("Could not read {0}: {1}".format(self.configfile, e), "Error")
        self.results = self.config.validate(self.validator, copy=True)
        if not self.results:
            for (section_list, key, _) in flatten_errors(self.config, self.results):
                if key is not None:
                    Logger.log('The {0} key in the section {1} failed validation'.format(key, ', '.join(section_list)), "ERROR")
                else:
                    Logger.log('The following section was missing:{0} '.format(', '.join(section_list)), "ERROR")

    def config_write(self):
        self.config.write()