from subprocess import call
import optparse

parser = optparse.OptionParser()
parser.set_defaults(maxindexes=10, seconds=3, jump=-1)
parser.add_option('-m', '--maxindexes', action='store', default=10, type='int', dest='maxindexes', help='Max number of terms to index. (default=10)')
parser.add_option('-s', '--seconds', action='store', default=0, type='int', dest='seconds', help='Seconds between indexes. (default=0)')
parser.add_option('-n', '--noreindex', action='store_true', default=False, dest='noreindex', help='No reindex, only pending. (default=False)')
(options, args) = parser.parse_args()

print('Indexing ' + str(options.maxindexes) + ' terms at a time, at a max rate of one every ' + str(options.seconds) + ' seconds with noreindex = ' + str(options.noreindex) + '.')

while True:
    call(['python', 'manage.py', 'index', '-p', '-m', str(options.maxindexes), '-s', str(options.seconds), '-x'])
    if not options.noreindex:
        call(['python', 'manage.py', 'index', '-r', '-m', str(options.maxindexes), '-s', str(options.seconds), '-x'])
