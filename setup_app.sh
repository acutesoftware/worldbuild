#!/bin/bash
########################################################
# setup_app.sh
# script to setup app - includes dependancies and config 
# mods needed.
########################################################

# install python packages
cd ~/dev/src/python/worldbuild/worldbuild/app
python -m venv venv_app
venv_app/bin/pip install pandas
venv_app/bin/pip install pathfinding
venv_app/bin/pip install matplotlib
