@echo off
setlocal

goto not37

python -V | find "3.7"
if errorlevel 1 goto not37
::python -V
echo pyinstaller only works with versions up to 3.6
pause
goto :eof

:not37
set path=c:\Python36;c:\Python36\scripts;%path%
set path=%path%;"C:\Program Files (x86)\Windows Kits\10\Redist\ucrt\DLLs\x64"

pyinstaller -v
@echo.


if exist env\scripts 	echo Using env\scripts 	
if exist env\scripts 	set path=env\Scripts;%path%
if not exist env\scripts	python.exe -m venv env && env/Scripts/activate && python -m pip install -r requirements.txt 

::   --debug=imports 
::  --clean 
::  --paths env\Lib\site-packages 
::  --hidden-import pygame.base 
::  --add-data resources\gearshift.ico;. ^
::  --add-data Grind_default.wav;. ^
::  --icon resources\gearshift.ico ^

rem --icon doesn't seem to do anything
rem --noconsole removes the console in the background but for now
rem             it's best to keep it for error messages
pyinstaller ^
  --onefile ^
  --distpath . ^
  --paths env\lib\site-packages ^
  "%~dp0\volumeControl.py "
pause

