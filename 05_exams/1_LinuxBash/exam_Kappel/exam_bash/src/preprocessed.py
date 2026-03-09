"""
-------------------------------------------------------------------------------
This script `preprocessed.py` retrieves data from the latest CSV file created 
in the 'data/raw/' directory.

1. It applies preprocessing to the data.
   
2. The results of the preprocessing are saved in a new CSV file 
   in the 'data/processed/' directory, with a name formatted as 
   'sales_processed_YYYYMMDD_HHMM.csv'.
   
3. All preprocessing steps are logged in the 
   'logs/preprocessed.logs' file to ensure detailed tracking of the process.

Any errors or anomalies are also logged to ensure traceability.
-------------------------------------------------------------------------------
"""

import pandas as pd
from datetime import datetime
import os

# Paths section
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_File = os.path.join(ROOT_DIR, "data", "raw", "sales_data.csv")
PROCESSED_DIR = os.path.join(ROOT_DIR, "data", "processed")
LOG_FILE = os.path.join(ROOT_DIR, "logs", "tests_logs", "test_preprocessed.logs")  # to change later



def preprocessing():
   """Reads the raw, perfomr mini cleaner dropna(),
      saves outpout csv with an stamp in dtaa/processed"""

   # File Opener inside preprocessing!
   with open(LOG_FILE, "a") as log:    #log for log mode
      log.write(f"{datetime.now()} --- Starting preprocessing\n")

   # Load war file 
   df = pd.read_csv(RAW_File)   # to be sure always last file

   # simple cleaner
   df = df.dropna()

   # existing dir
   os.makedirs(PROCESSED_DIR, exist_ok=True)            # no linux mkdir 

   # create (empty) ouput file
   timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")   # format lile testscropt
   output_file = os.path.join(PROCESSED_DIR, f"preprocessed_{timestamp}.csv")

   # concat df and scv once again
   df.to_csv(output_file, index=False)

   with open(LOG_FILE, "a") as log:
      log.write(f"{datetime.now()} - SAving processed file : {output_file}\n")
   return output_file



if __name__ == "__main__":
    preprocessing()
print("test")
