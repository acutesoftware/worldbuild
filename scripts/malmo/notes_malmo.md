# notes_malmo.md

Overview
--------------
These are notes on installing and playing with Microsoft Malmo library
to run AI applications on Minecraft.

My install of Minecraft is on Windows, so following windows install via 
https://github.com/Microsoft/malmo/blob/master/doc/install_windows.md


Status
----------
- installation works well, but had issues with python examples (I didnt have 2.7 setup as default)
- minecraft loads all mods correctly
- runs sample python bots well
- TODO - create own bots in worldbuild package

Running bots (after install)
------------------------------
1. start new command prompt
2. Launch Minecraft with mods
    `cd T:\user\dev\src\python\Malmo\Minecraft`
    `launchClient.bat`
    
3. Launch samples 
    `cd T:\user\dev\src\python\Malmo\Malmo\Python_examples`
    `c:\python27\python.exe ./run_mission.py`

Installation notes
------------------------

a. ffmpeg
Already have 7zip, so install 
from http://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-latest-win64-static.7z
and unzip to C:\ffmpeg

Add C:\ffmpeg\bin to path

b. codesynthesis
download xsd-4.0.msi
from http://www.codesynthesis.com/products/xsd/download.xhtml
install to (default)
C:\Program Files (x86)\CodeSynthesis XSD 4.0\ 

NOTE- may need to append a heap of paths and includes (see readme)


c. Python 2.7 
download 2.7.12 from https://www.python.org/downloads/
and install to C:\Python27 
(didnt prepend path as using 3.4 as default)

d. Java Development kit
install java (Java SE 8u91) from
http://www.oracle.com/technetwork/java/javase/downloads/index.html
to
C:\Program Files\Java\jdk1.8.0_91\

e. MS Runtime
Visit: https://www.microsoft.com/en-us/download/details.aspx?id=40784

Download vcredist_x64.exe and run. (already installed on this PC)

f. SlimDX (for human interaction component)
Install 64-bit .NET 4.0 download .msi file from  https://slimdx.org/download.php
 
g. download the Malmo release
git download from https://github.com/Microsoft/malmo
unzipped to T:\user\dev\src\python\Malmo

h. Launch with Mod
cd T:\user\dev\src\python\Malmo\Minecraft
launchClient.bat
(this took 29 min to install, then configure took 2 min 35sec, then another minute or so before Minecraft launches)

(Minecraft starts defaulting to port 10000 - sep install, WASD movement keys and mouse movement not on by default)



i. Run python agent
cd T:\user\dev\src\python\Malmo\Malmo\samples\Python_examples
c:\python27\python ./run_mission.py


Issues during install
-----------------------
Error - ImportError: No module named MalmoPython (forgot to reboot)

checked github issues, 

added "C:\Program Files (x86)\CodeSynthesis XSD 4.0\bin64" to path and rebooted

ran launchClient.bat - only took 27 seconds this time

import error again - realised I installed the wrong version of Python 32 bit, should be 
https://www.python.org/ftp/python/2.7.12/python-2.7.12.amd64.msi

Having issues running python examples - 

T:\user\dev\src\python\Malmo\Malmo\samples\Python_examples>.\run_mission.py
  File "T:\user\dev\src\python\Malmo\Malmo\samples\Python_examples\run_mission.py", line 59
    print "Error starting mission:",e
                                  ^
SyntaxError: invalid syntax

Changed to python 3 function syntax which was fine , but still says cant find module MalmoPython

  File "T:\user\dev\src\python\Malmo\Malmo\samples\Python_examples\run_mission.py", line 21, in <module>
    import MalmoPython
ImportError: No module named 'MalmoPython'

Tried to pip install (default python is now 2.7)

T:\user\dev\src\python\Malmo\Malmo\samples\Python_examples>pip install MalmoPython
Downloading/unpacking MalmoPython
  Could not find any downloads that satisfy the requirement MalmoPython
  
checked pypi - no module containing malmo so not on pip

Comment on Malmo issue - https://github.com/Microsoft/malmo/issues/166
2 others have same problem

Problem was fixed - the readme was updated to make sure we download the install not the build (I picked wrong one)
installed and unzipped to T:\user\dev\src\python\Malmo
ran launchClient ok
cd T:\user\dev\src\python\Malmo\Malmo\Python_examples  (original text - should have known when previous one had /samples/ in it)

ran run_mission and import MalmoPython now works ok
but still got print 'ERROR:',e SyntaxError

Fixed by explicity launching with Python2.7 as follows
c:\python27\python.exe ./run_mission.py





