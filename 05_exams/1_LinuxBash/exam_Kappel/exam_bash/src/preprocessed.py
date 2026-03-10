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

RAW_DIR = os.path.join(ROOT_DIR, "data", "raw")    # before it ws static file RAW_FILE which was for testing ok
PROCESSED_DIR = os.path.join(ROOT_DIR, "data", "processed")
LOG_FILE = os.path.join(ROOT_DIR, "logs", "preprocessed.logs")  # to change later (it was tets/logs/.....)



def preprocessing():
   """Reads the raw, perfomr mini cleaner dropna(),
      saves outpout csv with an stamp in dtaa/processed"""

   # File Opener inside preprocessing!
   with open(LOG_FILE, "a") as log:    #log for log mode
      log.write(f"{datetime.now()} --- Starting preprocessing\n")


   # RAW File
   files = [f for f in os.listdir(RAW_DIR) if f.startswith("sales_") and f.endswith(".csv") and f != "sales_data.csv"]
   latest = max(files, key=lambda f: os.path.getmtime(os.path.join(RAW_DIR, f)))
   RAW_File = os.path.join(RAW_DIR, latest)


   # Load war file 
   df = pd.read_csv(RAW_File)   # to be sure always last file

   # simple cleaner AND deleting timestamp due assert command in the tests scripts
   df = df.dropna()
   df = df.drop(columns = [col for col in df.columns if col =="timestamp"], errors="ignore")

   df["model"] = df["model"].astype("category").cat.codes      
   df = df.astype(int)


   # existing dir
   os.makedirs(PROCESSED_DIR, exist_ok=True)            # no linux mkdir command

   # create (empty) ouput file
   timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")   # format lile testscropt
   output_file = os.path.join(PROCESSED_DIR, f"sales_processed_{timestamp}.csv")   #sales_processed_ from testfile

   # concat df and scv once again
   df.to_csv(output_file, index=False)

   with open(LOG_FILE, "a") as log:
      log.write(f"{datetime.now()} - SAving processed file : {output_file}\n")
   return output_file


# gets executed only for debug
if __name__ == "__main__":
   preprocessing()
   print("test_final end")
