#!/bin/zsh
set -euo pipefail

TARGET_FILE="~/.zprofile"

cat payload >> ${TARGET_FILE} 
source ${TARGET_FILE} 

