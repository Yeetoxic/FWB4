#  Copyright (c) 2021 Yeetoxic

#Imports
import time


#-------------------------------------------------------
#Rate Limits (Temp. Module)
RATE_LIMIT = 2.0
last_request_time = 0.0


#-------------------------------------------------------
# Function to handle rate limits
def send_request():
    global last_request_time
    current_time = time.time()
    if current_time - last_request_time < RATE_LIMIT:
        time.sleep(RATE_LIMIT - (current_time - last_request_time))