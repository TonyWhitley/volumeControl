# https://www.pygame.org/docs/index.html
# pylint: disable=maybe-no-member
# warns about pygame.init() and pygame.JOYBUTTONDOWN etc.
import keyboard

import pygame


class Buttons:
    """
    Register for events from a joystick device.
    This is the base class.
    Call these functions specifying a string when the event occurs:
        register_for_button_press_event()
        register_for_axis_press_event()
        register_for_hat_press_event()
    then
        check_for_event()
    returns the user-defined string when an event occurs.
    """
    _registry = dict()
    _joysticks = dict()
    _errors = list()
    def __init__(self):
        """
        docstring
        """
        pygame.init()
        # called by init()    pygame.joystick.init()

        # Get count of joysticks
        self.joystick_count = pygame.joystick.get_count()

        # For each joystick:
        for i in range(self.joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()

            # Get the name from the OS for the controller/joystick
            _name = joystick.get_name().strip()
            self._joysticks[_name] = i
            self._registry[_name] = dict()
            self._registry[_name]['buttons'] = list()
            self._registry[_name]['axes'] = list()
            self._registry[_name]['hats'] = list()
            self._registry[_name]['num_buttons'] = joystick.get_numbuttons()
            self._registry[_name]['num_axes'] = joystick.get_numaxes()
            self._registry[_name]['num_hats'] = joystick.get_numhats()
        self._registry['keyboard'] = dict()
        self._registry['keyboard']['keys'] = list()

        """
        You can't use PyGame to generate key events without opening a visible
        display.  Instead, use keyboard to call callbacks when a key is
        pressed and then generate pygame events.
        """
        keyboard.add_hotkey('ctrl+c', self.ctrlc)

    def keyboard_callback(self, event):
        """
        keyboard library callback to get key events into the pygame event
        queue. pygame wants
        {'unicode': 'h', 'key': 104, 'mod': 0, 'scancode': 35, 'window': None}
        Do our best
        """
        _key_event = pygame.event.Event(pygame.KEYDOWN,
                                        unicode=event,
                                        scancode=35,
                                        key=None,   # can't (easily) calculate that
                                        mod=0,      # what is that?
                                        window=None
                                        )
        #_key_event_dict = {'unicode': 'h', 'key': 104, 'mod': 0, 'scancode': 35, 'window': None}
        pygame.event.post(_key_event)
    def ctrlc(self):
        """
        Ctrl/C pressed, generate a pygame QUIT event
        """
        _ctrlc = pygame.event.Event(pygame.QUIT)
        pygame.event.post(_ctrlc)


    def register_for_button_press_event(self,
                                       device: str,
                                       button: int,
                                       event_name: str):
        """
        Specify a button press we want to know about
        device: controller name
        button: 0-n the button/axis that is pressed
        event_name: the string that is returned when the event occurs
        """
        if device in self._joysticks:
            if button < self._registry[device]['num_buttons']:
                _t = (self._joysticks[device], button, event_name)
                self._registry[device]['buttons'].append(_t)
                return
            else:
                self._errors.append('Joystick "{}" does not have button {}'.
                                    format(device, button))
                return
        self._errors.append('Joystick "{}" not found'.format(device))

    def register_for_axis_press_event(self,
                                      device: str,
                                      axis: int,
                                      positive: bool,
                                      event_name: str):
        """
        Specify an axis change we want to know about
        device: controller name
        axis: 0-n the axis that is pressed
        positive: True for the + axis
        event_name: the string that is returned when the event occurs
        """
        if device in self._joysticks:
            if axis < self._registry[device]['num_axes']:
                _t = (self._joysticks[device], axis, positive, event_name)
                self._registry[device]['axes'].append(_t)
                return
            else:
                self._errors.append('Joystick "{}" does not have axis {}'.
                                    format(device, axis))
                return
        self._errors.append('Joystick "{}" not found'.format(device))

    def register_for_hat_press_event(self,
                                      device: str,
                                      hat: int,
                                      tup: (int,int),
                                      event_name: str):
        """
        Specify a hat button press we want to know about
        device: controller name
        hat: 0-n the hat button that is pressed
        positive: True for the + axis
        event_name: the string that is returned when the event occurs
        """
        if device in self._joysticks:
            if hat < self._registry[device]['num_hats']:
                _t = (self._joysticks[device], hat, tup, event_name)
                self._registry[device]['hats'].append(_t)
                return
            else:
                self._errors.append('Joystick "{}" does not have hat {}'.
                                    format(device, hat))
                return
        self._errors.append('Joystick "{}" not found'.format(device))

    def register_for_key_press_event(self,
                                      key: str,
                                      event_name: str):
        """
        Specify a key press we want to know about
        key: ASCII of the key that is pressed
        event_name: the string that is returned when the event occurs
        """
        _t = (key, event_name)
        self._registry['keyboard']['keys'].append(_t)
        keyboard.add_hotkey(key, self.keyboard_callback, args=key)

    def get_errors(self):
        """
        Return any errors in registering events
        """
        return self._errors

    def _parse(self, _event):
        """
        Check if _event is registered, return the user-defined string if so.
        """
        """
        Joystick button pressed.  {'joy': 1, 'button': 9}
        button
        Joystick axis moved.  {'joy': 1, 'axis': 0, 'value': -1.000030518509476}
        axis
        Joystick hat moved.  {'joy': 0, 'hat': 0, 'value': (-1, 0)}
        hat
        Key pressed.  {'unicode': 'h', 'key': 104, 'mod': 0, 'scancode': 35, 'window': None}
        key
        """
        if 'key' in _event:
            for _e in self._registry['keyboard']['keys']:
                if _e[0] == _event['unicode']:
                    return 'keyboard %s' % (_e[1])
        else:
            for device, joy in self._joysticks.items():
                if joy == _event['joy']:
                    if 'button' in _event:
                        for _e in self._registry[device]['buttons']:
                            if _e[0] == _event['joy']:
                                if _e[1] == _event['button']:
                                    return '%s %s' % (device, _e[2])
                    elif 'axis' in _event:
                        for _e in self._registry[device]['axes']:
                            if _e[0] == _event['joy']:
                                if _e[1] == _event['axis']:
                                    if _event['value'] > 0.5 and _e[2]:
                                        return _e[3]
                                    if _event['value'] < -0.5 and not _e[2]:
                                        return _e[3]
                    elif 'hat' in _event:
                        for _e in self._registry[device]['hats']:
                            if _e[0] == _event['joy']:
                                if _e[1] == _event['hat']:
                                    if _event['value'] == _e[2]:
                                        return _e[3]
                # else the event is not for this joystick
        return None

    def __debugPrint(self, dbgstr: str):
        #if 0:
        #    print(dbgstr)
        pass

    def check_for_event(self):
        """
        If a registered event has occurred, return the user-defined string
        specified for it.
        """
        result = None
        for _event in pygame.event.get(): # User did something
            if _event.type == pygame.QUIT:
                # If user clicked close
                result = "QUIT" # Flag that we are done
                                # Ctrl/C

            # print(pygame.event.event_name(_event.type))
            # Possible joystick actions:
            # JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
            if _event.type == pygame.JOYBUTTONDOWN:
                #print("Joystick button pressed. ", _event.dict)
                result = self._parse(_event.dict)
            if _event.type == pygame.JOYAXISMOTION:
                #print("Joystick axis moved. ", _event.dict)
                result = self._parse(_event.dict)
            if _event.type == pygame.JOYHATMOTION:
                #print("Joystick hat moved. ", _event.dict)
                result = self._parse(_event.dict)
            if _event.type == pygame.JOYBUTTONUP:
                self.__debugPrint("Joystick button released.")
            if _event.type == pygame.KEYDOWN:
                # Can't exit on Esc, that's pressed a lot in rFactor
                # so we'd keep on exiting this program.
                #if _event.dict['unicode'] == 'esc':
                #    result = "QUIT" # Flag that we are done
                #else:
                result = self._parse(_event.dict)


        return result


    def __del__(self):
        """
        # If you forget this line, the program will 'hang'
        # on exit if running from IDLE.
        """
        pygame.quit ()

def G25(Buttons_o):
    """
    Register for events from a Logitech G25 Racing Wheel (USB)
    """
    Buttons_o.register_for_button_press_event('Logitech G25 Racing Wheel USB', 0, '1') #etc.
    Buttons_o.register_for_button_press_event('Logitech G25 Racing Wheel USB', 4, 'Right paddle')
    Buttons_o.register_for_button_press_event('Logitech G25 Racing Wheel USB', 5, 'Left paddle')
    Buttons_o.register_for_button_press_event('Logitech G25 Racing Wheel USB', 6, 'Right wheel button')
    Buttons_o.register_for_button_press_event('Logitech G25 Racing Wheel USB', 7, 'Left wheel button')
    Buttons_o.register_for_button_press_event('Logitech G25 Racing Wheel USB', 8, '1st gear')
    Buttons_o.register_for_button_press_event('Logitech G25 Racing Wheel USB', 9, '2nd gear') #etc.
    Buttons_o.register_for_axis_press_event('Logitech G25 Racing Wheel USB', 0, True, 'Right')
    # It also has a hat
    Buttons_o.register_for_hat_press_event('Logitech G25 Racing Wheel USB', 0, (1,0), 'Right')
    Buttons_o.register_for_hat_press_event('Logitech G25 Racing Wheel USB', 0, (-1,0), 'Left')
    Buttons_o.register_for_hat_press_event('Logitech G25 Racing Wheel USB', 0, (0,1), 'Up')
    Buttons_o.register_for_hat_press_event('Logitech G25 Racing Wheel USB', 0, (0,-1), 'Down')

def keyboard_register(Buttons_o):
    Buttons_o.register_for_key_press_event('t', 'T')
    Buttons_o.register_for_key_press_event('#', 'hash')

def UsbGamepad(Buttons_o):
    """
    Register for events from a USB gamepad
    """
    Buttons_o.register_for_button_press_event('usb gamepad', 0, 'X')
    Buttons_o.register_for_button_press_event('usb gamepad', 1, 'A')
    Buttons_o.register_for_button_press_event('usb gamepad', 2, 'B')
    Buttons_o.register_for_button_press_event('usb gamepad', 3, 'Y')
    Buttons_o.register_for_button_press_event('usb gamepad', 4, 'Left')
    Buttons_o.register_for_button_press_event('usb gamepad', 5, 'Right')
    Buttons_o.register_for_button_press_event('usb gamepad', 8, 'Select')
    Buttons_o.register_for_button_press_event('usb gamepad', 9, 'Start')

    Buttons_o.register_for_axis_press_event('usb gamepad', 0, True, 'Right joystick')
    Buttons_o.register_for_axis_press_event('usb gamepad', 0, False, 'Left joystick')
    Buttons_o.register_for_axis_press_event('usb gamepad', 1, True, 'Down joystick')
    Buttons_o.register_for_axis_press_event('usb gamepad', 1, False, 'Up joystick')

if __name__ == '__main__':
    from text2speech import Text2Speech

    b_o = Buttons()
    UsbGamepad(b_o)
    G25(b_o)
    keyboard_register(b_o)
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()


    tts_o = Text2Speech()

    while 1:
        event = b_o.check_for_event()
        if event:
            _ev = event + ' pressed'
            print(_ev)
            tts_o.say(_ev)
        if event == "QUIT":
            break
        else:
            # Limit to 20 frames per second
            clock.tick(20)
    pass