from subprocess import call
import optparse

parser = optparse.OptionParser()
parser.set_defaults(seconds=5)
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
  'af': 2, 'an': 2, 'bs': 2, 'ca': 3, 'cs': 8,
  'cy': 2, 'da': 8, 'de': 50, 'el': 6, 'eo': 2,
  'es': 25, 'et': 4, 'eu': 2, 'fi': 6, 'fo': 2,
  'fr': 20, 'ga': 2, 'gl': 2, 'ha': 2, 'hr': 4,
  'hu': 4, 'is': 2, 'it': 15, 'la': 2, 'lb': 2,
  'lt': 3, 'lv': 2, 'mg': 2, 'mt': 2, 'nl': 15,
  'no': 5, 'oc': 2, 'pl': 8, 'pt': 12, 'qu': 2,
  'ro': 3, 'rw': 2, 'sk': 3, 'sl': 3, 'sn': 1,
  'so': 1, 'sv': 7, 'sw': 2, 'tr': 6, 'vo': 2,
  'wa': 2, 'wo': 1, 'xh': 2, 'yo': 1, 'zu': 1
}

while True:
    for x in range(100, -1, -1):
        for language in language_list:
            if language == 'en':
                continue
            lang_crawl_count = lang_crawl_counts.get(language, 10)
            call(['python', 'manage.py', 'crawl', '-r', '-m', str(lang_crawl_count), '-s', str(options.seconds), '-o', str(x * lang_crawl_count), '-l', language])
