from subprocess import call
import time

language_list = ['en', 'an', 'ca', 'cs', 'cy', 'da', 'de', 'el', 'es', 'et', 'eu', 'fi', 'fr', 'gl', 'ha', 'hr', 'hu', 'is', 'it', 'lt', 'lv', 'nl', 'no', 'pl', 'pt', 'ro', 'rw', 'sl', 'sn', 'so', 'sv', 'sw', 'tr', 'wo', 'xh', 'yo', 'zu']

# Index ratio controls how quickly we cycle through terms for a language.
# Counts for languages not in the index are ignored.
lang_index_counts = {'lt': 4, 'lv': 3, 'is': 4, 'sw': 2, 'yo': 2, 'so': 2, 'wo': 2, 'ha': 2, 'rw': 2, 'sn': 2, 'ca': 2, 'cs': 15, 'fi': 10, 'el': 10, 'hu': 8, 'pl': 10, 'tr': 14, 'da': 7, 'et': 4, 'de': 15, 'no': 5, 'pt': 10, 'nl': 8, 'sk': 8, 'sl': 8, 'es': 12, 'sv': 8, 'hr': 5, 'it': 8, 'fr': 12, 'ro': 6}

# Slowly indexes terms, one per minute maximum.
while True:
    for language in language_list:
        if language is 'en':
            continue
        # Reindex one old term for every 10 new terms being indexed.
        # We do things in larger batches than the en daemon in order to
        # take advantage of caching (which may or may not make a difference,
        # we haven't benchmarked anything).
        indexcount = lang_index_counts.get(language, 10)
        call(['python', 'manage.py', 'index', '-p', '-m', str(indexcount), '-s', '1', '-l', language])
        # Wait a few seconds between context switches
        time.sleep(1)
        call(['python', 'manage.py', 'index', '-r', '-m', str(indexcount), '-s', '1', '-l', language])
        # Wait a few seconds between cycles.
        time.sleep(1)
