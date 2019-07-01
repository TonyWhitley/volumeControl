import unittest
import config

test_defaults = {
    'nextprocess': {'device': 'usb gamepad',
             'type': 'button',
             'value': '0'},
    'volume_down': {'device': 'usb gamepad',
             'type': 'axis',
             'value': '-1'},
    'volume_up': {'device': 'usb gamepad',
             'type': 'hat',
             'value': '0,1'},
    'alt_volume_up': {'device': 'keyboard',   # (Keyboard example)
             'type': 'key',
             'value': 'a'},
    'processes': {'crewchiefv4.exe': '40, Crew Chief',
               'discord.exe': '70, Discord',
               'rfactor2.exe': '60, R Factor',
               'vlc.exe': '10, V L C'}}

class Test_test_config(unittest.TestCase):
    """
    Test the fetching of data from the config file
    """
    def setUp(self):
        self.config_o = config.Config(_defaults=test_defaults)
    def test_get_nextprocess(self):
        _nextprocess_device = self.config_o.get('nextprocess', 'device')
        assert _nextprocess_device == 'usb gamepad', _nextprocess_device
    def test_get_nextprocess_event(self):
        _nextprocess_event = self.config_o.get_event('nextprocess')
        assert _nextprocess_event == test_defaults['nextprocess'], _nextprocess_event

if __name__ == '__main__':
    unittest.main()
