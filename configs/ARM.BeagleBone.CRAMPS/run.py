#!/usr/bin/python
import sys
import os
import subprocess
import importlib
from machinekit import launcher
from time import *

launcher.register_exit_handler()
launcher.set_debug_level(5)
os.chdir(os.path.dirname(os.path.realpath(__file__)))
try:
    launcher.check_installation()  # make sure the Machinekit installation is sane
    launcher.cleanup_session()  # cleanup a previous session
    # Uncomment and modify the following line if you create a configuration for the BeagleBone Black
    #launcher.load_bbio_file('cramps_cape.bbio')  # load a BeagleBone Black universal overlay file
    # Uncomment and modify the following line of you have custom HAL components
    # launcher.install_comp('gantry.comp')  # install a comp HAL component if not already installed
    launcher.start_process("configserver ~/Machineface")  # start the configserver with Machineface an Cetus user interfaces
    launcher.start_process('linuxcnc DeltaForce-Face.ini')  # start linuxcnc
except subprocess.CalledProcessError:
    launcher.end_session()
    sys.exit(1)

# loop until script receives exit signal
# or one of the started applications exited incorrectly
# cleanup is done automatically

while True:
    sleep(1)
    launcher.check_processes()
