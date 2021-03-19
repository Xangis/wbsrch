from subprocess import call
import optparse

parser = optparse.OptionParser()
parser.set_defaults(seconds=5)
parser.add_option('-s', '--seconds', action='store', default=5, type='int', dest='seconds', help='Seconds between pages. (default=5)')
(options, args) = parser.parse_args()

while True:
    for x in range(100000, -20, -20):
        call(['python', 'manage.py', 'crawl', '-r', '-m', '20', '-s', str(options.seconds), '-o', str(x)])
