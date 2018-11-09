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
if [[ $EUID -ne 0 ]]; then
  echo "piot setup requires user to be root. su or sudo -s and run again ..."
  exit 1
fi
echo "user check complete"
#git clone https://github.com/ai-93/piot.git
#git checkout -b test
#pip3 install -r piot/requirements.txt
#python3 piot/setup_support.py