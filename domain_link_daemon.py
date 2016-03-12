from subprocess import call
import time
import random

SLEEP_TIME = 2

while True:
    # Reindex one term for every 10 new terms being indexed.
    call(['python', 'manage.py', 'domain_data_update', '-m', '250', '-s', str(SLEEP_TIME)])
    time.sleep(SLEEP_TIME)
    call(['python', 'manage.py', 'domain_data_update', '-r', '-m', '25', '-s', str(SLEEP_TIME)])
    time.sleep(SLEEP_TIME)
    
