from kaidame import *
from kaidame.Lib.configobj.configobj import ConfigObj, flatten_errors, ConfigObjError
from kaidame.Lib.configobj.validate import Validator


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
            kaidame.logger.log("Could not read {0}: {1}".format(self.configfile, e), "Error")
        self.results = self.config.validate(self.validator, copy=True)
        if not self.results:
            for (section_list, key, _) in flatten_errors(self.config, self.results):
                if key is not None:
                    kaidame.logger.log('The {0} key in the section {1} failed validation'.format(key, ', '.join(section_list)), "ERROR")
                else:
                    kaidame.logger.log('The following section was missing:{0} '.format(', '.join(section_list)), "ERROR")

    def config_write(self):
        self.config.write()