from subprocess import call
import optparse
import random

# Highest number of URLs in the pending table. Ideally we would query this.
# Raising this number is VERY expensive, to the tune of around 0.6 seconds per million rows
# scanned under moderate load.
MAX_URL = 1000000

parser = optparse.OptionParser()
parser.set_defaults(maxurls=10, seconds=3, jump=-1, offset=0)
parser.add_option('-m', '--maxurls', action='store', type='int', dest='maxurls', help='Max number of URLs to crawl. (default=100)')
parser.add_option('-s', '--seconds', action='store', type='int', dest='seconds', help='Seconds between pages. (default=3)')
parser.add_option('-o', '--offset', action='store', type='int', dest='offset', help='Record offset for start of crawl.')
(options, args) = parser.parse_args()

print('Crawling ' + str(options.maxurls) + ' URLs at a time, starting with ' + str(options.offset) + ' and skipping ahead ' + str(options.jump) + ' per cycle, at a rate of one every ' + str(options.seconds) + ' seconds.')

while True:
    call(['python', 'manage.py', 'crawl', '-p', '-m', str(options.maxurls), '-s', str(options.seconds), '-x'])
