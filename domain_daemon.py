from subprocess import call
import time

while True:
    # Update domains slowly to avoid annoying DNS servers. Do sequential, then random.
    call(['python', 'manage.py', 'domain_update', '-m', '1000', '-s', '10'])
    time.sleep(5)
    call(['python', 'manage.py', 'domain_update', '-m', '1000', '-s', '10', '-r'])
    time.sleep(5)

