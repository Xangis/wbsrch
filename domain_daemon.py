from subprocess import call
import time

while True:
    # Update domains slowly to avoid annoying DNS servers.
    call(['python', 'manage.py', 'domain_update', '-m', '20', '-s', '6', '-r'])
    time.sleep(5)
    
