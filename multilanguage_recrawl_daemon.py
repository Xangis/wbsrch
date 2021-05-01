from subprocess import call
import optparse

parser = optparse.OptionParser()
parser.set_defaults(seconds=5)
parser.add_option('-o', '--offset', action='store', default=0, type='int', dest='offset', help='Offset multiplier, 1 = skip one batch of urls, i.e. 1x20x100 for fr (default=0)')
parser.add_option('-s', '--seconds', action='store', default=5, type='int', dest='seconds', help='Seconds between pages. (default=5)')
(options, args) = parser.parse_args()

language_list = ['en', 'af', 'an', 'bs', 'ca', 'cs', 'cy', 'da', 'de', 'el',
                 'eo', 'es', 'et', 'eu', 'fi', 'fo', 'fr', 'ga', 'gl', 'ha',
                 'hr', 'hu', 'is', 'it', 'la', 'lb', 'lt', 'lv', 'mg', 'mt',
                 'nl', 'no', 'oc', 'pl', 'pt', 'qu', 'ro', 'rw', 'sk', 'sl',
                 'sn', 'so', 'sv', 'sw', 'tr', 'vo', 'wa', 'wo', 'xh', 'yo',
                 'zu']


# Based on a ratio vs French at 100,000 URLs wanting to recrawl 20 per round.
# Adjust accordingly as indexes evolve.
# Default is 1, which is appropriate for all small (<5k) indexes.
lang_crawl_counts = {
  'af': 1, 'an': 1, 'bs': 1, 'ca': 3, 'cs': 8,
  'cy': 1, 'da': 8, 'de': 50, 'el': 6, 'eo': 1,
  'es': 25, 'et': 2, 'eu': 1, 'fi': 7, 'fo': 1,
  'fr': 20, 'ga': 1, 'gl': 1, 'ha': 1, 'hr': 4,
  'hu': 8, 'is': 1, 'it': 15, 'la': 1, 'lb': 2,
  'lt': 3, 'lv': 2, 'mg': 1, 'mt': 1, 'nl': 15,
  'no': 6, 'oc': 1, 'pl': 12, 'pt': 18, 'qu': 1,
  'ro': 5, 'rw': 2, 'sk': 4, 'sl': 2, 'sn': 1,
  'so': 1, 'sv': 7, 'sw': 1, 'tr': 8, 'vo': 1,
  'wa': 1, 'wo': 1, 'xh': 1, 'yo': 1, 'zu': 1
}

while True:
    for x in range(100, -1, -1):
        for language in language_list:
            if language == 'en':
                continue
            lang_crawl_count = lang_crawl_counts.get(language, 10)
            offset = x * lang_crawl_count + (100 * lang_crawl_count * options.offset)
            call(['python', 'manage.py', 'crawl', '-r', '-m', str(lang_crawl_count), '-s', str(options.seconds), '-o', str(offset), '-l', language])
