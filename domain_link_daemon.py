from subprocess import call
import time
import random

SLEEP_TIME = 600

while True:
    # Update one existing domain for every 5 new domains being updated.
    #call(['python', 'manage.py', 'domain_data_update', '-m', '600', '-s', str(SLEEP_TIME)])
    call(['./domain_update', '10000', '0'])
    time.sleep(SLEEP_TIME)
    #call(['python', 'manage.py', 'domain_data_update', '-r', '-m', '120', '-s', str(SLEEP_TIME)])
    #time.sleep(SLEEP_TIME)

