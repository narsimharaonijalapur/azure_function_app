import logging
import azure.functions as func
from dotenv import load_dotenv
import time
import os
import base64
import requests
import datetime
load_dotenv()
from pathlib import Path
app = func.FunctionApp()
 
@app.timer_trigger(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=True, use_monitor=True)
def timer_mcsf_rag(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')
 
    # Retrieve the last run time from environment variable
    last_run_time_str = os.getenv('LAST_RUN_TIME')
    last_run_time = datetime.datetime.fromisoformat(last_run_time_str) if last_run_time_str else datetime.datetime.min
 
    # Process new files since the last run
    # check_and_process_files(last_run_time)
    print("Timer Trigger Execution Successful")
 
    # Make a function call
    # result = call_function()
    # logging.info(f'Function call result: {result}')
 
    # Update the last run time
    new_last_run_time = datetime.datetime.utcnow().isoformat()
    os.environ['LAST_RUN_TIME'] = new_last_run_time
 
    logging.info('Python timer trigger function executed.')
 
# Ensure logging is configured to capture logs at the info level or higher
logging.basicConfig(level=logging.INFO)
 
# if __name__ == "__main__":
#     app.run(port=8081)
has context menu
