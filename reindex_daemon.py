from subprocess import call
import time

while True:
    call(['python', 'manage.py', 'index', '-r', '-m', '10', '-s', '0', '-o', '100'])
    # Wait 5 seconds between cycles.
    time.sleep(1)
