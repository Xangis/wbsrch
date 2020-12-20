from subprocess import call
import time

while True:
    # Get them in batches of twenty, with a short break
    call(['python', 'manage.py', 'robots_update', '-m', '50', '-s', '0', '-i'])
    time.sleep(1)
