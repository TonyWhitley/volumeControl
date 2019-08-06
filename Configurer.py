# Set values in volumecontrol.ini that specify controls

import pygame
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font 

controls = {      #tkButton, 
                      #tkLabel, 
                            #tkStringVar, 
                                  #JoystickButton
  'Next program' : [None, None, None, 8],
  'Volume up' : [None, None, None, 9],
  'Volume down' : [None, None, None, 10]
  } 

class Controller:
  controllerNames = [
        'keyboard',
        'usb game controller'
        ]
  def __init__(self):
    pygame.init()

    self.num_controllers = pygame.joystick.get_count()
    if self.num_controllers < 1:
        self.error_string = 'No Controllers'
        self.error = True
        return

    self.controllerNames = []
    for j in range(self.num_controllers):
      _j = pygame.joystick.Joystick(j)
      self.controllerNames.append(self.get_name(_j))

  def get_name(self, controller):
    """
    pygame's get_name() can give an exception "invalid utf-8 character"
    """
    _name = 'Error getting controller name'
    try:
      _name = controller.get_name()
      print('get_name()') # DEBUG
      # _name = 'Logitech� G27 Shifter' # DEBUG 2
      # print('DEBUG pygame version: %s' % pygame.version.ver)
    except UnicodeError as e:
      print('Default locale') # DEBUG
      print(e.object.decode(locale.getdefaultlocale()[1])) # DEBUG
      _name = 'Unicode error getting controller name'
    except:
      _name = 'Other error getting controller name'
      print("Unexpected error:", sys.exc_info()[0])
    return _name

  def getAxis(self, axis):
    """ return 100 clutch released, 0 clutch pressed """
    axisValue = self.controller.get_axis(axis)
    # 1 is released, -1 is pressed
    return int((axisValue * 50)) + 50

  def getButtonState(self, buttonNumber):
    state = self.controller.get_button(buttonNumber)
    if state:
      result = 'D'
    else:
      result = 'U'
    return result

  def pygame_tk_check(self, callback, tk_main_dialog = None):
    """ Run pygame and tk to get latest events """
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            return
        # Possible controller actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYAXISMOTION:
            self.get_event()
            callback()
        if event.type == pygame.JOYBUTTONDOWN:
            self.get_event()
            callback()
        if event.type == pygame.JOYBUTTONUP:
            callback()
    if tk_main_dialog:  # Tk is running as well
      try:
        tk_main_dialog.update()
      except:
        pass # tk_main_dialog has been destroyed.

  def get_event(self):
    for j in range(self.num_controllers):
        _j = pygame.joystick.Joystick(j)
        self.controller = pygame.joystick.Joystick(j)

        self.controller.init()
        self.num_axes = self.controller.get_numaxes()
        self.axis_state = [0] * self.num_axes
        self.num_buttons = self.controller.get_numbuttons()
        self.controller_name = self.controller.get_name()    
        for g in range(self.num_buttons):
          if self.getButtonState(g) == 'D':
            return g

  def run(self, callback, tk_main_dialog = None):
    """ Run pygame and tk event loops """
    while 1:
      self.pygame_tk_check(callback, tk_main_dialog)
#########################
# The tab's public class:
#########################
class Tab:
  parentFrame = None
  controller_o = Controller() 
  xyPadding = 10

  def dummy(self):
    pass

  def __init__(self, parentFrame):
    """ Put this into the parent frame """
    self.parentFrame = parentFrame

    self.controls_o = controlsFrame(self.parentFrame)
    self.controls_o.tkFrame_Controls.grid(column=0, row=2, sticky='new', padx=self.xyPadding, rowspan=2)

    #############################
    buttonFont = font.Font(weight='bold', size=10)

    self.tkButtonSave = tk.Button(
        parentFrame,
        text="Save configuration",
        width=20,
        height=2,
        background='green',
        font=buttonFont,
        command=self.save)
    self.tkButtonSave.grid(column=1, row=3, pady=25)
    #############################

    self.controller_o.run(self.dummy, parentFrame)

  def controllerChoice(self, parent, tkvar):
    # List with options
    choices = self.controller_o.controllerNames

    tkvar.set(choices[0]) # set the default option
 
    popupMenu = tk.OptionMenu(parent, tkvar, *choices)
    tk.Label(parent, text="Choose a controller").grid(row = 0, column = 0)
    popupMenu.grid(row=0, column=1)
 
    #############################
    # on change dropdown value
    def change_dropdown(*args):
        name = tkvar.get()
        #self.controller_o.del()
        #!self.controller_o.selectController(name)

    # link function to change dropdown
    tkvar.trace('w', change_dropdown)

  def save(self):
    self.controls_o.save()
    self.clutch_o.save()

  def getSettings(self):
    """ Return the settings for this tab """
    return ['Options']

  def setSettings(self, settings):
    """ Set the settings for this tab """
    pass

class controlsFrame(Tab):
  tkFrame_Controls = None
  def __init__(self, parentFrame):
    #parentFrame = self.parentFrame
    self.tkFrame_Controls = tk.LabelFrame(parentFrame, text='Controls', padx=self.xyPadding,  pady=self.xyPadding)

    # Create a Tkinter variable
    self.controlsController = tk.StringVar(parentFrame)

    #self.controllerChoice(self.tkFrame_Controls, self.controlsController)

    ##########################################################
    for _control, (name, control) in enumerate(controls.items()):
      controls[name][0] = tk.Button(self.tkFrame_Controls, text='Select ' + name, width=15, 
                                 command=lambda n=name, w=super().controller_o: self.setControl(n,w))
      controls[name][0].grid(row = _control+2, sticky='w', pady=3)
      #! control[3] = super().config_o.get('controls', name)
      control[3] = 'name'
      controls[name][1] = tk.Label(self.tkFrame_Controls, 
                                text=control[3], fg = 'SystemInactiveCaptionText',
                                relief=tk.GROOVE, width=2,
                                borderwidth=4, anchor='e', padx=4)
      controls[name][1].grid(row = _control+2, column=1, sticky='w')
      controls[name][2] = tk.StringVar()
    for name, control in controls.items():
      #!control[2].set(super().config_o.get('controls', name))
      control[2] = 'nnname'

    #!self.controlsController.set(super().config_o.get('controls', 'controller'))

  def setControl(self, name, controller_o):
    messagebox.showinfo('', 'Select %s then press OK' % name)
    # Run pygame and tk to get latest input
    controller_o.pygame_tk_check(self.dummy, self.parentFrame)
    g = controller_o.get_event()
    if g:
        controls[name][2].set(g)
        controls[name][1].configure(text=str(g))
    else:
        messagebox.showerror('No control pressed', 'Input not changed')

  def save(self):
    self.config_o.set('controls','controller', self.controlsController.get())
    for name, control in controls.items():
      self.config_o.set('controls', name, control[2].get())


  
def main():
  root = tk.Tk()
  root.title('%s' % ('Control configurer'))
  tabOptions = ttk.Frame(root, width=1200, height=1200, relief='sunken', borderwidth=5)
  tabOptions.grid()
    
  o_tab = Tab(tabOptions)
  root.mainloop()

if __name__ == '__main__':
  # To run this tab by itself for development
  main()