from subprocess import call
import time
import optparse

parser = optparse.OptionParser()
parser.set_defaults(seconds=1)
parser.add_option('-n', '--noreindex', action='store_true', default=False, dest='noreindex', help='No reindex, only pending. (default=False)')
parser.add_option('-o', '--offset', action='store', default=0, type='int', dest='offset', help='Offset multiplier, 1 = skip one batch of indexes, i.e. 1x20 for fr (default=0)')
parser.add_option('-s', '--seconds', action='store', default=1, type='int', dest='seconds', help='Seconds between indexes. (default=1)')
(options, args) = parser.parse_args()

language_list = ['en', 'af', 'an', 'bs', 'ca', 'cs', 'cy', 'da', 'de', 'el', 'eo', 'es', 'et', 'eu', 'fi', 'fo', 'fr', 'ga', 'gl', 'ha', 'hr', 'hu', 'is', 'it', 'la', 'lb', 'lt', 'lv', 'mg', 'mt', 'nl', 'no', 'oc', 'pl', 'pt', 'qu', 'ro', 'rw', 'sk', 'sl', 'sn', 'so', 'sv', 'sw', 'tr', 'vo', 'wa', 'wo', 'xh', 'yo', 'zu']

# Index ratio controls how quickly we cycle through terms for a language.
# Counts for languages not in the index are ignored.
lang_index_counts = {
  'af': 2, 'an': 2, 'bs': 2, 'ca': 3, 'cs': 8,
  'cy': 2, 'da': 8, 'de': 30, 'el': 6, 'eo': 2,
  'es': 25, 'et': 4, 'eu': 2, 'fi': 6, 'fo': 2,
  'fr': 20, 'ga': 2, 'gl': 2, 'ha': 2, 'hr': 4,
  'hu': 4, 'is': 2, 'it': 15, 'la': 2, 'lb': 2,
  'lt': 3, 'lv': 2, 'mg': 2, 'mt': 2, 'nl': 15,
  'no': 5, 'oc': 2, 'pl': 8, 'pt': 12, 'qu': 2,
  'ro': 3, 'rw': 2, 'sk': 3, 'sl': 3, 'sn': 1,
  'so': 1, 'sv': 7, 'sw': 2, 'tr': 6, 'vo': 2,
  'wa': 2, 'wo': 1, 'xh': 2, 'yo': 1, 'zu': 1
}

# Slowly indexes terms, one per minute maximum.
while True:
    offset = options.offset
    for language in language_list:
        if language == 'en':
            continue
        # Reindex one old term for every 10 new terms being indexed.
        # We do things in larger batches than the en daemon in order to
        # take advantage of caching (which may or may not make a difference,
        # we haven't benchmarked anything).
        indexcount = lang_index_counts.get(language, 10)
        call(['python', 'manage.py', 'index', '-p', '-m', str(indexcount), '-s', str(options.seconds), '-l', language, '-o', str(options.offset * indexcount)])
        # Wait a few seconds between context switches
        time.sleep(options.seconds)
        if not options.noreindex:
            call(['python', 'manage.py', 'index', '-r', '-m', str(indexcount), '-s', str(options.seconds), '-l', language, '-o', str(options.offset * indexcount)])
            # Wait a few seconds between cycles.
            time.sleep(options.seconds)
