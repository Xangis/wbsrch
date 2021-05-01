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
  'af': 1, 'an': 1, 'bs': 1, 'ca': 3, 'cs': 12,
  'cy': 1, 'da': 10, 'de': 30, 'el': 9, 'eo': 1,
  'es': 26, 'et': 6, 'eu': 1, 'fi': 10, 'fo': 1,
  'fr': 22, 'ga': 1, 'gl': 1, 'ha': 1, 'hr': 8,
  'hu': 8, 'is': 4, 'it': 18, 'la': 1, 'lb': 1,
  'lt': 5, 'lv': 5, 'mg': 1, 'mt': 1, 'nl': 18,
  'no': 8, 'oc': 1, 'pl': 12, 'pt': 14, 'qu': 1,
  'ro': 7, 'rw': 1, 'sk': 2, 'sl': 5, 'sn': 1,
  'so': 1, 'sv': 10, 'sw': 1, 'tr': 10, 'vo': 1,
  'wa': 1, 'wo': 1, 'xh': 1, 'yo': 1, 'zu': 1
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
