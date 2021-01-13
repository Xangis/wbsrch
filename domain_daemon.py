from subprocess import call
import time

while True:
    # Update domains slowly to avoid annoying DNS servers. Do sequential, then random, then update old domains.
    call(['python', 'manage.py', 'domain_update', '-m', '20', '-s', '30'])
    time.sleep(5)
    call(['python', 'manage.py', 'domain_update', '-m', '20', '-s', '30', '-r'])
    time.sleep(5)
    call(['python', 'manage.py', 'domain_update', '-m', '20', '-s', '30', '-x'])
    time.sleep(5)
