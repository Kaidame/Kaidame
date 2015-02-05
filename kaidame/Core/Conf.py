__author__ = 'Dorbian'
# Configuration parser script
# Can run on anything, make a minor mod to the module you are running it in.
import kaidame
import os
import ConfigParser


class ConfigCheck():

    def __init__(self):
        self.configfile = ''
        self.results = ''
        self.config = ConfigParser.RawConfigParser()
        self.config.read(kaidame.configfile)
        if kaidame.developmentmode:
            self.logs = True
            kaidame.log("Loading config: {0}".format(kaidame.configfile), "DEBUG")

    # Check if the config key is an integer
    def check_int(self, sect, key, def_val, cset=False):
        if not cset:
            try:
                var_out = self.config.getint(sect, key)
            except ConfigParser.NoOptionError:
                var_out = def_val
                self.config.set(sect, key, def_val)

            if self.logs:
                kaidame.log('** Loaded INT: {0} : {1} -> {2} (Default {3})'.format(sect, key, var_out, def_val), 'DEBUG')

            return int(var_out)

        if cset:
            self.config.set(sect, key, def_val)
            kaidame.log('** Set INT: {0} : {1} to {2}'.format(sect, key, def_val), 'DEBUG')

    # Check if the config key is a boolean
    def check_bool(self, sect, key, def_val, cset=False):
        if not cset:
            try:
                var_out = self.config.getboolean(sect, key)
            except ConfigParser.NoOptionError:
                var_out = def_val
                self.config.set(sect, key, def_val)

            if self.logs:
                kaidame.log('** Loaded BOOL: {0} : {1} -> {2} (Default {3})'.format(sect, key, var_out, def_val), 'DEBUG')
            return bool(var_out)

        if cset:
            self.config.set(sect, key, def_val)
            kaidame.log('** Set BOOL: {0} : {1} to {2}'.format(sect, key, def_val), 'DEBUG')

    # Check if the config key is a float
    def check_float(self, sect, key, def_val, cset=False):
        if not cset:
            try:
                var_out = self.config.getfloat(sect, key)
            except ConfigParser.NoOptionError:
                var_out = def_val
                self.config.set(sect, key, def_val)

            if self.logs:
                kaidame.log('** Loaded FLOAT: {0} : {1} -> {2} (Default {3})'.format(sect, key, var_out, def_val), 'DEBUG')
            return float(var_out)

        if cset:
            self.config.set(sect, key, def_val)
            kaidame.log('** Set FLOAT: {0} : {1} to {2}'.format(sect, key, def_val), 'DEBUG')

    # Check if the config key is a string
    def check_str(self, sect, key, def_val, cset=False):
        if not cset:
            try:
                var_out = self.config.get(sect, key)
            except ConfigParser.NoOptionError:
                var_out = def_val
                self.config.set(sect, key, def_val)

            if self.logs and not cset:
                kaidame.log('** Loaded STR: {0} : {1} -> {2} (Default {3})'.format(sect, key, var_out, def_val), 'DEBUG')
            return str(var_out)

        if cset:
            self.config.set(sect, key, def_val)
            kaidame.log('** Set STR: {0} : {1} to {2}'.format(sect, key, def_val), 'DEBUG')

    # Check if section exists
    def CheckSec(self, sec):
        if self.config.has_section(sec):
            if self.logs:
                kaidame.log('* Loaded Section: {0}'.format(sec), 'DEBUG')
                return True
        else:
            self.config.add_section(sec)

    # Write configuration to file
    def config_write(self):
        with open(kaidame.configfile, 'wb') as configfile:
            self.config.write(configfile)
        if self.logs:
            kaidame.log('* Wrote Config: {0}'.format(kaidame.configfile), 'DEBUG')

    # Custom Kaidame Addition:
    # Check for files in the module dir and subdirs, and add them to the config file if needed.
    def find_module(self):
        for dirname, dirnames, filenames in os.walk(kaidame.moduledir):
            # print path to all subdirectories first.
            for subdirname in dirnames:
                section = os.path.basename(os.path.normpath(subdirname))
                location = os.path.join(kaidame.moduledir, subdirname)
                self.CheckSec(section)

                for dirname, dirnames, filenames in os.walk(location):
                    for filename in filenames:
                        if '__init__.py' in filename:
                            pass
                        else:
                            section = os.path.basename(os.path.normpath(subdirname))
                            filenameq, fileextension = os.path.splitext(filename)
                            self.check_bool(section, filenameq, "False")
                            try:
                                modval = self.config.getboolean(section, filenameq)
                                kaidame.modules.update({filenameq: {'Location': location, "Section": section, "State": modval}})
                            except AttributeError:
                                modval = False
                                kaidame.modules.update({filenameq: {'Location': location, "Section": section, "State": modval}})