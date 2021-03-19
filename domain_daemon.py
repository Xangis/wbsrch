from subprocess import call
import time
import optparse

parser = optparse.OptionParser()
parser.set_defaults(seconds=30)
parser.add_option('-s', '--seconds', action='store', default=30, type='int', dest='seconds', help='Seconds between domain lookups. (default=30)')
(options, args) = parser.parse_args()

while True:
    # Update domains slowly to avoid annoying DNS servers. Do sequential, then random, then update old domains.
    call(['python', 'manage.py', 'domain_update', '-m', '100', '-s', str(options.seconds)])
    time.sleep(5)
    call(['python', 'manage.py', 'domain_update', '-m', '100', '-s', str(options.seconds), '-r'])
    time.sleep(5)
    call(['python', 'manage.py', 'domain_update', '-m', '100', '-s', str(options.seconds), '-x'])
    time.sleep(5)
