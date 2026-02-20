#!/bin/zsh
set -euo pipefail

TARGET_FILE="/Users/${USER}/.zprofile"

cat payload >> ${TARGET_FILE} 
source ${TARGET_FILE} 
