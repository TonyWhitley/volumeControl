import json
import pygame   # https://www.pygame.org/docs/index.html

import unittest

controllerName = 'usb gamepad'

class Test_config(unittest.TestCase):
    """
    Test the fetching of data from the config file
    """
    def setUp(self):
        self.dict = {
            'nextProcess': {
                'controllerName': 'usb gamepad',
                'button': 0},
            'previousProcess': {
                'controllerName': 'usb gamepad',
                'button': 1},
            'volumeUp': {
                'controllerName': 'usb gamepad',
                'button': 2},
            'volumeDown': {
                'controllerName': 'usb gamepad',
                'button': 3},
            'processNames': ['rFactor 2.exe', 'discord.exe', 'crewchief.exe']
            }
        with open("volumeControldata.json", "w") as volumeControl_data_file:
            json.dump(self.dict, volumeControl_data_file, indent=4, sort_keys=True)

    def test_read_config_button_bindings(self):
        assert self.dict['nextProcess']['controllerName'] == 'usb gamepad'
    def test_read_config_process_list(self):
        assert self.dict['processNames'] == ['rFactor 2.exe', 'discord.exe', 'crewchief.exe']

class Test_process(unittest.TestCase):
    """
    Test the reading of Windows processes 
    and matching the ones of interest
    """
    def test_get_process_id(self):
        """
        get the ID of a specified process
        """
        pass
    def test_no_such_process(self):
        """
        Process specified is not running
        """
        pass
    def test_next_process(self):
        """
        'next' when current process is not the last in the list
        """
        pass
    def test_next_process_wrap_round(self):
        """
        'next' when current process is the last in the list
        """
        pass

class Test_button_monitor(unittest.TestCase):
    """
    Test that pressing buttons on the controller
    causes the event:
    Next process
    Previous process maybe?
    Volume up
    Volume down

    Test button does not exist
    """
    def test_get_controller(self):
        """
        Get a Joystick object by name
        """
        pygame.joystick.init()
        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        

        for j in joysticks:
            if j.get_name().strip() == controllerName:
                return j
        assert False, 'Controller "%s" not found' % controllerName

class Test_volumeControl(unittest.TestCase):
    """
    Test the setting of the volume in Windows processes 
    (Verify by reading it back)
    """
    def test_set_volume(self):
        """
        Set the volume of a process
        """
        pass

    def test_set_volume(self):
        """
        Set the volume of a process
        """
        pass

class Test_gui(unittest.TestCase):
    """
    Test the GUI
    """
    def test_status_window(self):
        """
        Send messages to the status window
        (the only window)
        """
        pass

if __name__ == '__main__':
    unittest.main()
