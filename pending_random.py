from subprocess import call
import optparse

parser = optparse.OptionParser()
parser.set_defaults(maxurls=100, seconds=3)
parser.add_option('-m', '--maxurls', action='store', type='int', dest='maxurls', help='Max number of URLs to crawl. (default=100)')
parser.add_option('-s', '--seconds', action='store', type='int', dest='seconds', help='Seconds between pages. (default=3)')
(options, args) = parser.parse_args()

print('Crawling ' + str(options.maxurls) + ' URLs at a time, at a rate of one every ' + str(options.seconds) + ' seconds.')

while True:
    call(['python', 'manage.py', 'crawl', '-p', '-m', str(options.maxurls), '-s', str(options.seconds), '-x'])
