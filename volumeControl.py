# pylint: disable=invalid-name
"""
Use controller buttons or keyboard keys to control the volume of
a set of processes.  Use case is an online racing game with
associated programs for speech and for an AI assistant (rFactor 2,
Discord, Crew Chief) and in particular in VR where it's hard to
adjust the volume.

Design notes:
Using the pygame library https://www.pygame.org/docs/index.html
which provides events when controller buttons are pressed.

That is used for the GUI too simply because it offers it.
Maybe not, tkinter will be more suitable - but initially just
print to the console.

The main function is button_monitor() which is a callback function
called by pygame when a button is pressed. It then calls functions
that handle the buttons:
'Next' button: select_process()
'Previous' (if required): ditto
'Up' button:   setVolume()
'Down' button: setVolume()

select_process() gets a list of processes from getProcess() which
provides handles for each process.

setVolume() alters the current volume for the current process, either
increasing it or decreasing it by an amount specified in the
configuration.

statusDisplay() shows the volume set for each process. It also shows
a warning if a specified process is not actually running and an error
message if a specified button is not found.

There is a class for reading and writing configuration items from/to
a data file.
"""

from buttonMonitor import Buttons
from config import Config
import status_display

NEXT_PROCESS = 'nextProcess'
VOLUME_UP = 'volume_up'
VOLUME_DOWN= 'volume_down'

def button_monitor():
    """
    Read button configuration
    Set up callbacks to
    * select_process()
    * setVolume()
    Report error if button not found
    """
    _config_o = Config()
    _section = 'buttons'
    _controller =  _config_o.get(_section, 'controller')
    _nextProcess = int(_config_o.get(_section, NEXT_PROCESS))
    _volume_up =   int(_config_o.get(_section, VOLUME_UP))
    _volume_down = int(_config_o.get(_section, VOLUME_DOWN))
    Buttons_o = Buttons()
    Buttons_o.register_for_button_press_event(_controller, _nextProcess, NEXT_PROCESS)
    Buttons_o.register_for_button_press_event(_controller, _volume_up,   VOLUME_UP)
    Buttons_o.register_for_button_press_event(_controller, _volume_down, VOLUME_DOWN)

    return Buttons_o

class Processes:
    """
    docstring
    """
    _current_process = 0
    _processes = list()
    def __init__(self):
        """
        Read list of process names
        Find each process
        """
        #'processes'
        self._processes = ['rFactor 2.exe','discord.exe','crewchief.exe']
    def select(self): # Next process
        """
        docstring
        """
        self._current_process += 1
        self._current_process %= len(self._processes)

    def get(self):
        """
        docstring
        """
        return self._processes[self._current_process]

class Volume:
    """
    docstring
    """
    def __init__(self, processes):
        """
        Read initial volume levels for each process
        Set them
        Read volume step
        """
        self.process = processes[0]
        self.volume = 50
        self.tts_o = Text2Speech()

    def set_current_process(self, process):
        """
        docstring
        """
        self.process = process
        _vol_str = 'Current process is %s' % self.process
        self.tts_o.say(_vol_str)
    def volume_up(self):
        """
        Increase volume of current process
        """
        if self.volume < (101 - 10):
            self.volume += 10
        _vol_str = '%s volume set to %d' % (self.process, self.volume)
        self.tts_o.say(_vol_str)
    def volume_down(self):
        """
        Decrease volume of current process
        """
        if self.volume > 10:
            self.volume -= 10
        _vol_str = '%s volume set to %d' % (self.process, self.volume)
        self.tts_o.say(_vol_str)

if __name__ == "__main__":
    from text2speech import Text2Speech

    tts_o = Text2Speech()

    buttons_o   = button_monitor()
    processes_o = Processes()
    next_p = processes_o.get()
    volume_o    = Volume(processes_o._processes)
    volume_o.set_current_process(next_p)

    while 1:
        event = buttons_o.check_for_event() 
        if event:
            _ev = 'Gamepad ' + event + ' pressed'
            print(_ev)
            #tts_o.say(_ev)
            if event == NEXT_PROCESS:
                processes_o.select()
                next_p = processes_o.get()
                volume_o.set_current_process(next_p)
            if event == VOLUME_UP:
                volume_o.volume_up()
            if event == VOLUME_DOWN:
                volume_o.volume_down()

    pass