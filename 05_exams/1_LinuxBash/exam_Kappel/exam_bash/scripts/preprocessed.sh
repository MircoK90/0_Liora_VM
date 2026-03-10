#!/bin/bash

# =============================================================================
# This script preprocessed.sh runs the program src/preprocessed.py
# and logs the execution details in the log file
# logs/preprocessed.logs.
# =============================================================================

# start: exam_bash/scripts/preprocessed.sh




LOG_FILE="logs/preprocessed.logs"                                           #no " "
echo "$(date '+%Y-%m-%d %H:%M:%S') - preprocessing ..." >> $LOG_FILE

python src/preprocessed.py             #backbone works almost always
echo "$(date '+%Y-%m-%d %H:%M:%S') - preprocessing finished." >> $LOG_FILE    #attention to the +
