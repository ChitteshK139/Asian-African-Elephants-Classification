import os
import sys
import logging

# custom logging
logging_str="[%(asctime)s %(levelname)s: %(module)s: %(message)s]"

log_dir="logs"
log_filepath=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    # Provides to view logs at both places
    handlers=[
        logging.FileHandler(log_filepath),     # read the log file (file handler)
        logging.StreamHandler(sys.stdout)      # Print log on terminal
    ]
)

logger=logging.getLogger("Asian_African_Elephants_ClassificationLogger")
