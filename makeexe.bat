@echo off

call pyInstallerSetup env

::   --debug=imports 
::  --clean 
::  --paths env\Lib\site-packages 
::  --hidden-import pygame.base 

rem --icon doesn't seem to do anything
rem --noconsole removes the console in the background but for now
rem             it's best to keep it for error messages
pyinstaller ^
  --onefile ^
  --distpath . ^
  --paths envPygame\lib\site-packages ^
  --hidden-import pyttsx3.drivers ^
  --hidden-import pyttsx3.drivers.sapi5 ^
  "%~dp0\volumeControl.py "
pause

