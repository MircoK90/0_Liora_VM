#!/bin/bash
# Bash Comand obligatory LINE!!!
# ==============================================================================
# Script: collect.sh
# Description:
#   This script queries an API to retrieve sales data for the following graphics card models:
#     - rtx3060
#     - rtx3070
#     - rtx3080
#     - rtx3090
#     - rx6700
#
#   The collected data is appended to a copy of the file:
#     data/raw/sales_data.csv
#
#   The output file is saved in the format:
#     data/raw/sales_YYYYMMDD_HHMM.csv
#   with the following columns:
#     timestamp, model, sales
#
#   Collection activity (requests, queried models, results, errors)
#   is recorded in a log file:
#     logs/collect.logs
#
#   The log should be human-readable and must include:
#     - The date and time of each request
#     - The queried models
#     - The retrieved sales data
#     - Any possible errors
# ==============================================================================




RAW_DIR="data/raw"
LOG_FILE="logs/collect.logs"

# Create Folder if not there
mkdir -p "$RAW_DIR"
mkdir -p "logs"

# filecreation
timestamp=$(date '+%Y%m%d_%H%M%S')      # plus inside!  WITHOUT " "!!!!!!
file="$RAW_DIR/sales_$timestamp.csv"    

#Start wih loggin for collectiopn
echo "$(date '+%Y-%m-%d %H:%M:%S') - Collection Data ... " >> "$LOG_FILE"




# cp to concat new data from api, 
latest=$(ls -t "$RAW_DIR"/sales_2*.csv 2>/dev/null | head -1)
if [ -z "$latest" ]; then
    cp "$RAW_DIR/sales_data.csv" "$file"                        # use sales_data
else
    cp "$latest" "$file"                                        # use last created file (date)
fi
echo "" >> "$file"                                              # newline to keep format due concatineng

# API integration
MODELS=("rtx3060" "rtx3070" "rtx3080" "rtx3090" "rx6700") # as LIST!


for model in "${MODELS[@]}"; do
    sales=$(curl -s "http://0.0.0.0:5000/$model")
    ts=$(date '+%Y-%m-%dT%H:%M:%SZ')

    echo "$ts,$model,$sales" >> "$file"
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $model: $sales" >> "$LOG_FILE"
done


echo "$(date '+%Y-%m-%d %H:%M:%S') - Saved: $file" >> "$LOG_FILE"
















# # mk test
# cat <<EOF > "$file"
# timestamp,model,sales
# 2025-04-25T09:06:57Z,rtx3060,13
# 2025-04-25T09:06:57Z,rtx3070,17
# 2025-04-25T09:06:57Z,rtx3080,17
# 2025-04-25T09:06:57Z,rtx3090,14
# 2025-04-25T09:06:57Z,rx6700,16
# EOF