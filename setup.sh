#!/usr/bin/env bash
#################################################################################
# Installation script for piot
#
# Licensed under GNU General Public License v3.0 GPL-3 (in short)
#
#   You may copy, distribute and modify the software as long as you track
#   changes/dates in source files. Any modifications to our software
#   including (via compiler) GPL-licensed code must also be made available
#   under the GPL along with build & install instructions.
#
#################################################################################
printf "\n User Permission check \n ########################## \n"
if [[ $EUID -ne 0 ]]; then
  echo "piot setup requires user to be root. su or sudo -s and run again ..."
  exit 1
fi
printf "\n User Permission check completed successfully \n ##########################\n"
printf "\n Cloning piot repo \n ##########################\n"
apt-get -y install git
git clone https://github.com/ai-93/piot.git
git checkout pihole-mqtt
cd piot
printf "\n Cloning piot repo completed successfully \n ##########################\n"
printf "\n Installing python dependencies \n ##########################\n"
pip3 install -r requirements.txt
printf "\n Installing python dependencies completed successfully \n ##########################\n"
printf "\n Setup piot \n ##########################\n"
python3 setup_support.py
printf "\n Setup piot completed successfully \n ##########################\n"
