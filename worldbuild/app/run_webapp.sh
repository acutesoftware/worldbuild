#!/bin/bash
########################################################
# run_webapp.sh
# Run the app in the virtual environment
########################################################

cd /home/duncan/dev/src/python/worldbuild/worldbuild/app
source venv_app/bin/activate
python app_web.py
