"""
docstring
"""
from configparser import ConfigParser
from os.path import exists
import pprint

CONFIG_FILE_NAME = 'volumeControl.ini'

defaults = {
    'buttons': {'controller': 'usb gamepad',
             'nextprocess': '0',
             'volume_down': '2',
             'volume_up': '1'},
    'processes': {'crewchiefv4.exe': '40, Crew Chief',
               'discord.exe': '70, Discord',
               'rfactor2.exe': '60, R Factor',
               'vlc.exe': '10, V L C'}}

new_defaults = {
    'nextprocess': {'device': 'usb gamepad',
             'type': 'button',
             'value': '0'},
    'volume_down': {'device': 'usb gamepad',
             'type': 'axis',
             'value': '-1'},
    'volume_up': {'device': 'usb gamepad',
             'type': 'hat',
             'value': '0,1'},
    'volume_up': {'device': 'keyboard',   # (Keyboard example)
             'type': 'key',
             'value': 'a'},
    'processes': {'crewchiefv4.exe': '40, Crew Chief',
               'discord.exe': '70, Discord',
               'rfactor2.exe': '60, R Factor',
               'vlc.exe': '10, V L C'}}

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
        for section in defaults.keys():
            for val, default in defaults[section].items():
                self.set(section, val, default)
        # if there is an existing file parse values over those
        if exists(CONFIG_FILE_NAME):
            self.config.read(CONFIG_FILE_NAME)
            pprint.pprint({section: dict(self.config[section]) for section in self.config.sections()})
        else:
            self.write()
            self.config.read(CONFIG_FILE_NAME)
        pass

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
