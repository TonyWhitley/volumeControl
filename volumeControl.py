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

from config import Config
import status_display

def button_monitor(button_event):
    """
    Read button configuration
    Set up callbacks to
    * select_process()
    * setVolume()
    Report error if button not found
    """
    pass

class Processes:
    """
    docstring
    """
    def __init__(self):
        """
        Read list of process names
        Find each process
        """
    def select(self): # Next process
        """
        docstring
        """
        pass
    def get(self):
        """
        docstring
        """
        pass

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
    def set_current_process(self, process):
        """
        docstring
        """
        self.process = process
    def volume_up(self):
        """
        Increase volume of current process
        """
        pass
    def volume_down(self):
        """
        Decrease volume of current process
        """
        pass

if __name__ == "__main__":
    _config_o = Config()
    _section = 'buttons'
    _val = 'controller'
    _value = _config_o.get(_section, _val)
