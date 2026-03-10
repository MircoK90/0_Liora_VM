#!/bin/bash
# -----------------------------------------------------------------------------
# This script train.sh runs the Python program src/train.py.
# This program trains a prediction model and saves the final model
# in the model/ directory. The script also logs all execution details
# in the file logs/train.logs.
# -----------------------------------------------------------------------------




LOG_FILE="logs/train.logs"    # NO " "!!!!

echo "$(date '+%Y-%m-%d %H:%M:%S') - Training is Running ..." >> "$LOG_FILE"

python3 src/train.py    # python3 works on every machine without venv
echo "$(date '+%Y-%m-%d %H:%M:%S') - Training finished." >> "$LOG_FILE"make