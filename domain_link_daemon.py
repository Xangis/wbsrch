from subprocess import call
import time

# Runs 6 times per day, so at 60,000 adds and 60,000 updates per day we add or update 3.6 million domains per month at a maximum.
SLEEP_TIME = 7200

while True:
    # Update new domains first, then old.
    call(['./domain_update', '10000', '0'])
    time.sleep(SLEEP_TIME)
    call(['./domain_update', '10000', '0', 'Y'])
    time.sleep(SLEEP_TIME)
