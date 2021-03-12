from subprocess import call
import time

SLEEP_TIME = 3600

while True:
    # Update new domains first, then old.
    call(['./domain_update', '100000', '0'])
    time.sleep(SLEEP_TIME)
    call(['./domain_update', '200000', '0', 'Y'])
    time.sleep(SLEEP_TIME)
