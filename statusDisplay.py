import pygame

class StatusDisplay:
    def __init__(self, processNames):
        """
        Create frame
        """
        pygame.init()
 
        # Set the width and height of the screen [width,height]
        size = [500, 700]
        screen = pygame.display.set_mode(size)

        pygame.display.set_caption("Volume control")

        #Loop until the user clicks the close button.
        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
    def __del__(self):
        # Close the window and quit.
        # If you forget this line, the program will 'hang'
        # on exit if running from IDLE.
        pygame.quit ()

    def processNotFound(self, processName):
        pass
    def buttonNotFound(self, buttonName):
        pass
    def currentProcess(self, processName):
        pass
    def displayVolume(self, volume):
        pass
