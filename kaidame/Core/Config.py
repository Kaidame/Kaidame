import kaidame
from kaidame import *
#resolved through path update
from configobj import ConfigObj, ConfigObjError, flatten_errors
from validate import Validator

#example-----------------------------------
# from configobj import ConfigObj
# config = ConfigObj(filename)
# #
# value1 = config['keyword1']
# value2 = config['keyword2']
# #
# section1 = config['section1']
# value3 = section1['keyword3']
# value4 = section1['keyword4']
# #
# # you could also write
# value3 = config['section1']['keyword3']
# value4 = config['section1']['keyword4']
#------------------------------------------


class ConfigCheck():

    def __init__(self):
        self.configfile = kaidame.configfile
        self.config = None
        self.results = None
        self.validator = Validator()
        self.specdir = os.path.join(os.path.join(os.path.join(rundir, 'kaidame'), 'Core'), "configspec.ini")

    def config_validate(self):
        try:
            self.config = ConfigObj(configspec=self.specdir, file_error=True)
            self.config.filename = self.configfile
        except (ConfigObjError, IOError), e:
            kaidame.log("Could not read {0}: {1}".format(self.configfile, e), "Error")
        self.results = self.config.validate(self.validator, copy=True)
        if not self.results:
            for (section_list, key, _) in flatten_errors(self.config, self.results):
                if key is not None:
                    kaidame.log('The {0} key in the section {1} failed validation'.format(key, ', '.join(section_list)), "ERROR")
                else:
                    kaidame.log('The following section was missing:{0} '.format(', '.join(section_list)), "ERROR")

    def config_write(self):
        self.config.write()

    def config_get(self):
