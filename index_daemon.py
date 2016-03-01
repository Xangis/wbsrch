from subprocess import call
import time

while True:
    # Reindex one term for every 10 new terms being indexed.
    call(['python', 'manage.py', 'index', '-p', '-m', '10', '-s', '0'])
    # Wait 5 seconds between context switches
    time.sleep(1)
    call(['python', 'manage.py', 'index', '-r', '-m', '10', '-s', '0'])
    # Wait 5 seconds between cycles.
    time.sleep(1)
    
