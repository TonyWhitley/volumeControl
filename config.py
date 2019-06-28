"""
docstring
"""
from configparser import ConfigParser
from os.path import exists

CONFIG_FILE_NAME = 'volumeControl.ini'
sections = ['buttons', 'processes']
button_values = {
    'controller'        : 'usb gamepad',
    'nextProcess'       : '0',
    'volume_up'         : '1',
    'volume_down'       : '2'
    }
process_names = {
    'rFactor2.exe'      : '40, R Factor',
    'discord.exe'       : '50, Discord',
    'crewchiefv4.exe'   : '60, Crew Chief'
    }

class Config:
    """
    docstring
    """
    def __init__(self):
        """
        # instantiate
        """
        self.config = ConfigParser()

        # set default values
        for val, default in button_values.items():
            self.set('buttons', val, default)
        for val, default in process_names.items():
            self.set('processes', val, default)
    
        # if there is an existing file parse values over those
        if exists(CONFIG_FILE_NAME):
            self.config.read(CONFIG_FILE_NAME)
        else:
            self.write()
            self.config.read(CONFIG_FILE_NAME)

    def set(self, section, val, value):
        """
        # update existing value
        """
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, val, value)

    def get(self, section, val):
        """
        # get value
        """
        try:
            # get existing value
            #if val in ['controller'] :
            return self.config.get(section, val)
            #else:
            #return self.config.getint(section, val)
        except Exception as e: #NoSectionError: # No such section in file
            self.set(section, val, '')
            return None

    def get_all(self, section):
        """
        # get all the keys in section
        """
        _keys = list()
        try:
            for _key in self.config[section]:
                _keys.append(_key)

        except Exception as e: #NoSectionError: # No such section in file
            pass
        return _keys

    def write(self):
        """
        # save to a file
        """
        with open(CONFIG_FILE_NAME, 'w') as configfile:
            self.config.write(configfile)

if __name__ == "__main__":
    _config_o = Config()
    _section = 'buttons'
    _val = 'controller'
    _value = _config_o.get(_section, _val)
    if _value:
        if _val == 'controller':
            print('%s/%s: %s' % (_section, _val, _value))
        else:
            print('%s/%s: %d' % (_section, _val, _value))
    else:
        print('%s/%s: <None>' % (_section, _val))
        _config_o.write()

    _section = 'processes'
    for key in  _config_o.get_all(_section):
        print(key)

    pass
