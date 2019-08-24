"""
Configure the user events that drive the program
"""
# pylint: disable=maybe-no-member
# warns about pygame.init() and pygame.JOYBUTTONDOWN etc.
import pygame
from buttonMonitor import Buttons
from wx_configurer_gui import Configurer

class Inputs(Buttons):
    def __init__(self):
        super().__init__()

    def get(self):
        result = None
        #if not pygame.key.get_focused():
        #    print('NOT pygame.key.get_focused()')
        for _event in pygame.event.get(): # User did something
            if _event.type == pygame.QUIT:
                # If user clicked close
                result = "QUIT" # Flag that we are done
                                # Ctrl/C

            # print(pygame.event.event_name(_event.type))
            # Possible joystick actions:
            # JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
            if _event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed. ", _event.dict)
                result = 'button'
            if _event.type == pygame.JOYAXISMOTION:
                if abs(_event.value) > 0.1:
                    print("Joystick axis moved. ", _event.dict)
                    result = 'axis'
            if _event.type == pygame.JOYHATMOTION:
                print("Joystick hat moved. ", _event.dict)
                result = 'hat'
            if _event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")
            if _event.type == pygame.KEYDOWN:
                print("Key pressed. ", _event.dict)
                #print(_event.key) # == pygame.K_ESCAPE)
                result = 'key'
        return result

def text(_text):
    # define the RGB value for white,
    #  green, blue colour .
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    # assigning values to X and Y variable
    X = 400
    Y = 400

    # create the display surface object
    # of specific dimension..e(X, Y).
    display_surface = pygame.display.set_mode((X, Y ))

    # set the pygame window name
    pygame.display.set_caption('Configure buttons')

    # create a font object.
    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.Font('freesansbold.ttf', 18)

    # create a text suface object,
    # on which text is drawn on it.
    _text = font.render(_text, True, green, blue)

    # create a rectangular object for the
    # text surface object
    textRect = _text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (X // 2, Y // 2)

    # completely fill the surface object
    # with white color
    display_surface.fill(white)

    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    display_surface.blit(_text, textRect)

    # Draws the surface object to the screen.
    pygame.display.update()

def main():
    inputs_o = Inputs()

    configurer_gui = Configurer(0)
    configurer_gui.MainLoop()

    pygame.display.set_mode((512,384))
    text('Press key for "Next program"')

    while 1:
        event = inputs_o.get()
        if event:
            print(event)
            #break

    text('Press key for "Volume up"')

    while 1:
        event = inputs_o.get()
        if event:
            print(event)
            break

    text('Press key for "Volume down"')

    while 1:
        event = inputs_o.get()
        if event:
            print(event)
            break

if __name__ == "__main__":
    main()

