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


#!/bin/bash

RAW_DIR = "data/raw"
LOG_FILE = "logs/collect.logs"

mkdir -p "$RAW_DIR"
mkdir -p "logs"

# filevreation
timestamp = $(date '+%Y%m%d_%H%M%S')      # plus inside!
file = "$RAW_DIR/sales_$timestamp.csv"    

echo "$(date '+%Y-%m-%d %H:%M:%S') - Collection Data ... " >> "$LOG_FILE"

# mk test
cat <<EOF > "$file"
timestamp,model,sales
2025-04-25T09:06:57Z,rtx3060,13
2025-04-25T09:06:57Z,rtx3070,17
2025-04-25T09:06:57Z,rtx3080,17
2025-04-25T09:06:57Z,rtx3090,14
2025-04-25T09:06:57Z,rx6700,16
EOF

echo "$(date '+%Y-%m-%d %H:%M:%S') - Collection Saved " >> "$LOG_FILE"

