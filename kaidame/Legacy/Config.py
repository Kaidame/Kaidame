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
        self.configfile = ''
        kaidame.log("Loading config: {0}".format(self.configfile), "DEBUG")
        self.results = ''
        self.validator = Validator()
        self.spec = os.path.join(os.path.join(os.path.join(rundir, 'kaidame'), 'Core'), "configspec.ini")
        self.config = ''

    def config_validate(self):
        self.results = self.config.validate(self.validator, copy=True)
        if not self.results:
            for (section_list, key, _) in flatten_errors(self.config, self.results):
                if key is not None:
                    kaidame.log('The {0} key in the section {1} failed validation'.format(key, ', '.join(section_list)), "ERROR")
                else:
                    kaidame.log('The following section was missing:{0} '.format(', '.join(section_list)), "ERROR")

    def config_read(self):
        #try:
        self.config = ConfigObj(configspec=self.spec, file_error=True)
        self.config.filename = kaidame.configfile
        #except (ConfigObjError, IOError), e:
            #kaidame.log("Could not read {0}: {1}".format(self.configfile, e), "Error")

    def config_write(self):
        self.config.write()

    def CheckSec(self, sec):
        try:
            self.config[sec]
            return True
        except:
            self.config[sec] = {}
            return False

    def check_int(self, cfg_name, item_name, def_val, logs=True):
        try:
            print "integer {0} {1} {2}".format(cfg_name, item_name, def_val)
            my_val = int(self.config[cfg_name][item_name])
            print "integer {0} {1} {2}".format(cfg_name, item_name, my_val)
        except:
            my_val = def_val
            try:
                self.config[cfg_name][item_name] = my_val
            except:
                self.config[cfg_name] = {}
                self.config[cfg_name][item_name] = my_val

        if logs:
            kaidame.log(item_name + " -> " + str(my_val), "DEBUG")
        else:
            kaidame.log(item_name + " -> ******", "DEBUG")
        return my_val

    def check_str(self, cfg_name, item_name, def_val, logs=True):
        try:
            my_val = self.config[cfg_name][item_name]
        except:
            my_val = def_val
            try:
                self.config[cfg_name][item_name] = my_val
            except:
                self.config[cfg_name] = {}
                self.config[cfg_name][item_name] = my_val

        if logs:
            kaidame.log(item_name + " -> " + my_val, "DEBUG")
        else:
            kaidame.log(item_name + " -> ******", "DEBUG")
        return my_val

    def check_bool(self, cfg_name, item_name, def_val, logs=True):
        try:
            my_val = int(self.config[cfg_name][item_name])
        except:
            my_val = def_val
            try:
                self.config[cfg_name][item_name] = my_val
            except:
                self.config[cfg_name] = {}
                self.config[cfg_name][item_name] = my_val

        my_val = bool(my_val)

        if logs:
            kaidame.log(item_name + " -> " + str(my_val), "DEBUG")
        else:
            kaidame.log(item_name + " -> ******", "DEBUG")
        return my_val

    def configbuild(self):
        self.config_read()
        self.config_validate()
        self.config_write()