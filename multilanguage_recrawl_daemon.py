from subprocess import call
import optparse

parser = optparse.OptionParser()
parser.set_defaults(seconds=5)
parser.add_option('-s', '--seconds', action='store', default=5, type='int', dest='seconds', help='Seconds between pages. (default=5)')
(options, args) = parser.parse_args()

language_list = ['en', 'an', 'ca', 'cs', 'cy', 'da', 'de', 'el', 'es', 'et', 'eu', 'fi', 'fr', 'gl', 'ha', 'hr', 'hu', 'is', 'it', 'lt', 'lv', 'nl', 'no', 'pl', 'pt', 'ro', 'rw', 'sl', 'sn', 'so', 'sv', 'sw', 'tr', 'wo', 'xh', 'yo', 'zu']


# Based on a ratio vs French at 100,000 URLs wanting to recrawl 20 per round.
# Adjust accordingly as indexes evolve.
# Default is 1, which is appropriate for all small (<5k) indexes.
lang_crawl_counts = {
  'cs': 3, 'fr': 20, 'nl': 10, 'de': 50, 'hu': 2, 'it': 15, 'pl': 8, 'pt': 3, 'ro': 2, 'es': 14, 'sv': 7, 'tr': 5
}

while True:
    for x in range(100, -1, -1):
        for language in language_list:
            if language == 'en':
                continue
            lang_crawl_count = lang_crawl_counts.get(language, 1)
            call(['python', 'manage.py', 'crawl', '-r', '-m', str(lang_crawl_count), '-s', str(options.seconds), '-o', str(x * lang_crawl_count), '-l', language])
