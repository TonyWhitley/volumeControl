"""
User feedback
"""

class StatusDisplay:
    """
    User feedback
    """
    # pylint: disable=missing-docstring
    # pylint: disable=no-self-use
    def __init__(self, _process_names):     # process_names are not used in
                                            # this simple print implementation
        pass
    def process_not_found(self, process_name):
        print(f"Warning: process '{process_name}' not running")
    def button_not_found(self, button_name):
        print(f"Error: button '{button_name}' not found")
    def current_process(self, process_name):
        print(f"Current process '{process_name}'")
    def display_volume(self, volume):
        print(f"Volume: {volume}")
