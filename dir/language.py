from django.core.exceptions import ObjectDoesNotExist
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from dir.utils import GetRootUrl, GetDomainExtension
from dir.models import DomainSuffix, language_list, blocked_language_list, language_names, blocked_language_names
from bs4 import BeautifulSoup
from dir.exceptions import InvalidLanguageException
from langid.langid import LanguageIdentifier, model
identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
from urllib.parse import urlparse

language_name_reverse = {
'catalan': 'ca',
'english': 'en',
'german': 'de',
'deutsch': 'de',
'francais': 'fr',
'french': 'fr',
'spanish': 'es',
'polish': 'pl',
'italian': 'it',
'dutch': 'nl',
'portuguese': 'pt',
'turkish': 'tr',
'turkce': 'tr',
'czech': 'cs',
'romanian': 'ro',
'greek': 'el',
'swedish': 'sv',
'danish': 'da',
'hungarian': 'hu',
'croatian': 'hr',
'slovak': 'sk',
'slovakian': 'sk',
'lithuanian': 'lt',
'norwegian': 'no',
'finnish': 'fi',
'estonian': 'et',
'latvian': 'lv',
'slovene': 'sl',
'slovenian': 'sl',
'icelandic': 'is',
'swahili': 'sw',
'yoruba': 'yo',
'somali': 'so',
'wolof': 'wo',
'hausa': 'ha',
'rwandan': 'rw',
'kinyarwanda': 'rw',
'shona': 'sn',
'galician': 'gl',
'basque': 'eu',
}

def GetInfixLanguage(url, descriptive=False):
    # Remove query parameters from the URL before testing.
    parsedurl = urlparse(url)
    url = parsedurl.scheme + '://' + parsedurl.netloc.lower() + parsedurl.path + parsedurl.params
    # fr
    for language in language_list:
        if ('/' + language + '/') in url:
            if descriptive:
                print('Selected language {0} using /fr/ method'.format(language))
            return language
        # FR
        if ('/' + language.upper() + '/') in url:
            if descriptive:
                print('Selected language {0} using /FR/ method'.format(language))
            return language
        # Fr
        if ('/' + language[0].upper() + language[1:] + '/') in url:
            if descriptive:
                print('Selected language {0} using /Fr/ method'.format(language))
            return language
        # Lang_FR (www.spamfighter.com, for example)
        if ('/Lang_' + language.upper() + '/') in url:
            if descriptive:
                print('Selected language {0} using /Lang_FR/ method'.format(language))
            return language
    # fr-fr
    for language in locales:
        if ('/' + language[1] + '/') in url:
            if descriptive:
                print('Selected language {0} using /fr-fr/ method'.format(language[0]))
            return language[0]
    # fr_fr
    for language in locales:
        underscored = language[1].replace('-', '_')
        if ('/' + underscored + '/') in url:
            if descriptive:
                print('Selected language {0} using /fr-fr/ method'.format(language[0]))
            return language[0]
    # fr-FR and fr_FR
    for language in locales:
        if '-' in language[1]:
            pieces = language[1].split('-')
            uppercased = pieces[0] + '-' + pieces[1].upper()
            if ('/' + uppercased + '/') in url:
                if descriptive:
                    print('Selected language {0} using /fr-FR/ method'.format(language[0]))
                return language[0]
            uppercased_under = pieces[0] + '_' + pieces[1].upper()
            if ('/' + uppercased_under + '/') in url:
                if descriptive:
                    print('Selected language {0} using /fr_FR/ method'.format(language[0]))
                return language[0]
    # fr.fr
    for language in locales:
        underscored = language[1].replace('-', '.')
        if ('/' + underscored + '/') in url:
            if descriptive:
                print('Selected language {0} using /fr.fr/ method'.format(language[0]))
            return language[0]
    # br-pt (reversed locale, carreraworld.com uses this)
    for language in locales:
        pieces = list(reversed(language[1].split('-')))
        underscored = '-'.join(pieces)
        if ('/' + underscored + '/') in url:
            if descriptive:
                print('Selected language {0} using /br-pt/ method (reversed locale)'.format(language[0]))
            return language[0]
    # br_pt (reversed locale, ftt.roto-frank.com uses this)
    for language in locales:
        pieces = list(reversed(language[1].split('-')))
        underscored = '_'.join(pieces)
        if ('/' + underscored + '/') in url:
            if descriptive:
                print('Selected language {0} using /br_pt/ method (reversed locale)'.format(language[0]))
            return language[0]
    # /french
    for language in list(language_name_reverse.keys()):
        if ('/' + language) in url:
            if descriptive:
                print('Selected language {0} using /french method'.format(language_name_reverse[language]))
            return language_name_reverse[language]
    if '/gahuza' in url:
        if descriptive:
            print('Selected language rw using /gahuza method')
        return 'rw'
    # /fr
    for language in language_list:
        if url.endswith('/' + language):
            if descriptive:
                print('Selected language {0} using /fr method'.format(language))
            return language
    # /french/
    for language in list(language_names.keys()):
        if ('/' + language_names[language].lower() + '/') in url:
            if descriptive:
                print('Selected language {0} using /french/ method'.format(language))
            return language
    # /fre/
    for language in list(language_names.keys()):
        if ('/' + language_names[language][0:3].lower() + '/') in url:
            if descriptive:
                print('Selected language {0} using /fre/ method'.format(language))
            return language
    if '/us/' in url or '/gb/' in url:
        if descriptive:
            print('Selected language en using /us/ or /gb/')
        return 'en'
    if '/mx/' in url:
        if descriptive:
            print('Selected language es using /mx/')
        return 'es'
    if '/br/' in url:
        if descriptive:
            print('Selected language pt using /br/')
        return 'pt'
    if '/cz/' in url:
        if descriptive:
            print('Selected language cs using /cz/')
        return 'cs'
    if '/se/' in url:
        if descriptive:
            print('Selected language sv using /se/')
        return 'sv'
    # /ru/
    for language in blocked_language_list:
        if ('/' + language + '/') in url:
            if descriptive:
                print('Selected invalid language {0} using /ru/ method'.format(language))
            raise InvalidLanguageException(language)
        # RU
        if ('/' + language.upper() + '/') in url:
            if descriptive:
                print('Selected invalid language {0} using /RU/ method'.format(language))
            raise InvalidLanguageException(language)
        # Ru
        if ('/' + language[0].upper() + language[1:] + '/') in url:
            if descriptive:
                print('Selected invalid language {0} using /Ru/ method'.format(language))
            raise InvalidLanguageException(language)
        # Lang_RU (www.spamfighter.com, for example)
        if ('/Lang_' + language.upper() + '/') in url:
            if descriptive:
                print('Selected invalid language {0} using /Lang_RU/ method'.format(language))
            raise InvalidLanguageException(language)
    # /ru-ru/
    for language in blocked_locales:
        if ('/' + language[1] + '/') in url:
            if descriptive:
                print('Selected invalid language {0} using /ru-ru/ method'.format(language))
            raise InvalidLanguageException(language[0])
    # Ends with /ru
    for language in blocked_language_list:
        if url.endswith('/' + language):
            if descriptive:
                print('Selected invalid language {0} using /ru method'.format(language))
            raise InvalidLanguageException(language)
    # /russian/
    for language in list(blocked_language_names.keys()):
        if ('/' + language + '/') in url:
            if descriptive:
                print('Selected invalid language {0} using /russian/ method'.format(blocked_language_names[language]))
            raise InvalidLanguageException(blocked_language_names[language])
    # ru-RU and ru_RU
    for language in blocked_locales:
        if '-' in language[1]:
            pieces = language[1].split('-')
            uppercased = pieces[0] + '-' + pieces[1].upper()
            if ('/' + uppercased + '/') in url:
                if descriptive:
                    print('Selected invalid language {0} using /ru-RU/ method'.format(language[0]))
                return language[0]
            uppercased_under = pieces[0] + '_' + pieces[1].upper()
            if ('/' + uppercased_under + '/') in url:
                if descriptive:
                    print('Selected invalid language {0} using /ru_RU/ method'.format(language[0]))
                return language[0]
    if descriptive:
        print('No infix language found. Returning None.')
    return None

def GetUrlParameterLanguage(url):
    lang = None
    parsedurl = urlparse(url)
    if parsedurl.query:
        queryparams = dict(urlparse.parse_qsl(parsedurl.query))
        if 'lang' in queryparams:
            lang = queryparams['lang']
        elif 'Lang' in queryparams:
            lang = queryparams['Lang']
        elif 'language' in queryparams:
            lang = queryparams['language']
        elif 'lan' in queryparams:
            lang = queryparams['lan']
        elif 'setLang' in queryparams:
            lang = queryparams['setLang']
        elif 'hl' in queryparams:
            lang = queryparams['hl']
        elif 'lg' in queryparams:
            lang = queryparams['lg']
        elif 'loc' in queryparams:
            lang = queryparams['loc']
    if lang and '-' in lang:
        lang = lang.split('-')[0]
    if lang and '_' in lang:
        lang = lang.split('_')[0]
    # Not sure how these could get messed up this way, but they can, somehow.
    # Maybe there was a crawler problem at one point...
    if lang == "[u'en']":
        lang = 'en'
    if lang == "[u'es']":
        lang = 'es'
    if lang == "[u'pt']":
        lang = 'pt'
    if lang == "[u'nl']":
        lang = 'nl'
    if lang == "[u'pl']":
        lang = 'pl'
    if lang == "[u'fr']":
        lang = 'fr'
    if lang == "[u'de']":
        lang = 'de'
    if lang == "[u'tr']":
        lang = 'tr'
    if lang == "[u'it']":
        lang = 'it'
    if lang not in language_list:
        if lang in language_name_reverse:
            lang = language_name_reverse[lang]
    return lang


# List of languages and the domain extensions to search for and trust when they declare a language in the page.
languages = {
             'cs': ['.cz'],
             'da': ['.da'],
             'de': ['.de', '.at', '.ch', '.lu'],
             'el': ['.gr', '.cy'],
             'es': ['.mx', '.es', '.pe', '.cl', '.ar', '.co', '.bo', '.gt', '.ni', '.pa', '.cr', '.ec', '.py', '.uy', '.ve', '.pr', '.cu', '.do', '.dm', '.hn', '.sv', '.cv'],
             'et': ['.ee'],
             'fi': ['.fi'],
             'fr': ['.fr', '.cm', '.ch', '.be', '.cd', '.cf', '.cg', '.dj', '.ga', '.ci', '.gf', '.gq', '.gn', '.ht', '.lu', '.ml', '.mq', '.ne', '.pf', '.re', '.rw', '.sn', '.td', '.tg', '.tn'],
             'hr': ['.hr'],
             'hu': ['.hu'],
             'is': ['.is'],
             'it': ['.it', '.sm', '.va'],
             'lv': ['.lv'],
             'lt': ['.lt'],
             'nl': ['.nl', '.be', '.gy', '.sr', '.sx'],
             'no': ['.no'],
             'pl': ['.pl'],
             'pt': ['.pt', '.br', '.mz', '.ao'],
             'ro': ['.ro', '.md'],
             'sk': ['.sk'],
             'sl': ['.si'],
             'sv': ['.sw'],
             'tr': ['.tr'],
             'sw': ['.tz'],
            }

language_blocks = {
             'ar': ['.eg', '.ae', '.ir', '.iq', '.sa', '.om', '.ly', '.pk', '.tr', '.er', '.km', '.dz', '.ma', '.sd', '.ye', '.sy', '.tn', '.so', '.jo', '.lb', '.kw', '.mr', '.qa', '.af', '.bh', '.bn', '.dj', '.mr'],
             'az': ['.az'],
             'bg': ['.bg'],
             'hy': ['.am'],
             'id': ['.id'],
             'he': ['.il'],
             'il': ['.il'],
             'jp': ['.jp'], # Mistagged pages are somewhat common.
             'ja': ['.jp'],
             'ka': ['.ge'],
             'ko': ['.kp', '.ko', '.asia'],
             'mn': ['.mn'],
             'my': ['.my'],
             'ru': ['.ru', '.by', '.kz', '.kg', '.ua', '.uz', '.tm', '.bg', '.et', '.lv', '.lt', '.md', '.am', '.ge', '.su', '.tj'],
             'tg': ['.ph'],
             'th': ['.th'],
             'uk': ['.ua', '.md'],
             'vn': ['.vn'], # Mistagged pages are somewhat common.
             'vi': ['.vn'],
             'zh': ['.cn', '.sg', '.hk', '.mo', '.asia'],
            }


locales = [
           ['ca', 'ca-es', '.es'],
           ['cs', 'cs-cz', '.cz'],
           ['da', 'da-dk', '.dk'],
           ['de', 'de-de', '.de'],
           ['de', 'de-at', '.at'],
           ['el', 'el-gr', '.gr'],
           ['en', 'en-in', '.in'],
           ['en', 'en-au', '.au'],
           ['en', 'en-ca', '.ca'],
           ['en', 'en-nz', '.nz'],
           ['en', 'en-za', '.za'],
           ['en', 'en-gb', '.uk'],
           ['en', 'en-uk', '.uk'],
           ['en', 'en-us', '.com'],
           ['es', 'es-es', '.es'],
           ['es', 'es-mx', '.mx'],
           ['es', 'es-ar', '.ar'],
           ['es', 'es-cl', '.cl'],
           ['es', 'es-co', '.co'],
           ['es', 'es-mx', '.mx'],
           ['es', 'es-pe', '.pe'],
           ['es', 'es-uy', '.uy'],
           ['es', 'es-pa', '.pa'],
           ['es', 'es-pa', '.py'],
           ['et', 'et-ee', '.ee'],
           ['eu', 'eu-ad', '.ad'],
           ['eu', 'eu-es', '.es'],
           ['eu', 'eu-fr', '.fr'],
           ['fi', 'fi-fi', '.fi'],
           ['fr', 'fr-ch', '.ch'],
           ['fr', 'fr-fr', '.fr'],
           ['fr', 'fr-tn', '.tn'],
           ['fr', 'fr-ag', '.ag'],
           ['fr', 'fr-ca', '.ca'],
           ['gl', 'gl-es', '.es'],
           ['hr', 'hr-hr', '.hr'],
           ['hu', 'hu-hu', '.hu'],
           ['is', 'is-is', '.is'],
           ['it', 'it-it', '.it'],
           ['it', 'it-it', '.sm'],
           ['lt', 'lt-lt', '.lt'],
           ['lv', 'lv-lv', '.lv'],
           ['nl', 'nl-nl', '.nl'],
           ['no', 'nb-no', '.no'],
           ['no', 'no-no', '.no'],
           ['no', 'nb', '.no'],
           ['no', 'nn', '.no'],
           ['pl', 'pl-pl', '.pl'],
           ['pt', 'pt-pt', '.pt'],
           ['pt', 'pt-br', '.br'],
           ['ro', 'ro-ro', '.ro'],
           ['ro', 'ro-md', '.md'],
           ['sk', 'sk-sk', '.sk'],
           ['sl', 'sl-si', '.si'],
           ['sv', 'sv-se', '.se'],
           ['sv', 'sw-se', '.se'], # Wrong, but some Swedish sites incorrectly use the "sw" code.
           ['sv', 'sw', '.se'],
           ['sw', 'sw-ug', '.ug'],
           ['sw', 'sw-tz', '.tz'],
           ['sw', 'sw-ke', '.ke'],
           ['tr', 'tr-tr', '.tr'],
]

blocked_locales = [
           ['ar', 'ar-eg', '.eg'],
           ['ar', 'ar-ae', '.ae'],
           ['ar', 'ar-ir', '.ir'],
           ['ar', 'ar-iq', '.iq'],
           ['ar', 'ar-sa', '.sa'],
           ['ar', 'ar-om', '.om'],
           ['ar', 'ar-ly', '.ly'],
           ['ar', 'ar-pk', '.pk'],
           ['ar', 'ar-tr', '.tr'],
           ['ar', 'ar-er', '.er'],
           ['ar', 'ar-km', '.km'],
           ['ar', 'ar-dz', '.dz'],
           ['ar', 'ar-ma', '.ma'],
           ['ar', 'ar-sd', '.sd'],
           ['ar', 'ar-ye', '.ye'],
           ['ar', 'ar-sy', '.sy'],
           ['ar', 'ar-tn', '.tn'],
           ['ar', 'ar-tn', '.tn'],
           ['ar', 'ar-so', '.so'],
           ['ar', 'ar-jo', '.jo'],
           ['ar', 'ar-lb', '.lb'],
           ['ar', 'ar-kw', '.kw'],
           ['ar', 'ar-mr', '.mr'],
           ['ar', 'ar-qa', '.qa'],
           ['ar', 'ar-af', '.af'],
           ['ar', 'ar-bh', '.bh'],
           ['ar', 'ar-bn', '.bn'],
           ['ar', 'ar-dj', '.dj'],
           ['az', 'az-az', '.az'],
           ['bg', 'bg-bg', '.bg'],
           ['hy', 'hy-am', '.am'],
           ['id', 'id-id', '.id'],
           ['il', 'il-il', '.il'],
           ['mn', 'mn-mn', '.mn'],
           ['my', 'my-my', '.my'],
           ['jp', 'jp-ja', '.jp'],
           ['jp', 'jp-jp', '.jp'], # Mistagged pages are somewhat common.
           ['ka', 'ka-ge', '.ge'],
           ['ko', 'ko-ko', '.ko'],
           ['ko', 'ko-kp', '.kp'],
           ['ru', 'ru-by', '.by'],
           ['ru', 'ru-kg', '.kg'],
           ['ru', 'ru-kz', '.kz'],
           ['ru', 'ru-ru', '.ru'],
           ['ru', 'ru-tj', '.tj'],
           ['ru', 'ru-tm', '.tm'],
           ['ru', 'ru-ua', '.ua'],
           ['ru', 'ru-uz', '.uz'],
           ['tg', 'tg-ph', '.ph'],
           ['th', 'th-th', '.th'],
           ['uk', 'uk-ua', '.ua'],
           ['uk', 'uk-md', '.md'],
           ['vi', 'vn-vi', '.vn'],
           ['vi', 'vn-vn', '.vn'], # Mistagged pages are somewhat common.
           ['zh', 'zh-cn', '.cn'],
           ['zh', 'zh-hk', '.hk'],
           ['zh', 'zh-sg', '.sg'],

]

def IdentifyPageLanguage(url, html):
    url = url.lower()
    html = html.lower()
    prefix = None
    lang = None
    suffixlangs = []
    infixlangs = []
    rooturl = GetRootUrl(url)
    # First we extract what we can from the URL
    for lang in list(languages.keys()):
        if rooturl.startswith(lang + '.'):
            prefix = lang
            break
    if not prefix:
        for lang in list(language_blocks.keys()):
            if rooturl.startswith(lang + '.'):
                prefix = lang
                break
    for lang in list(languages.keys()):
        for suffix in languages[lang]:
            if rooturl.endswith(suffix):
                suffixlangs.append(lang)
    for lang in list(language_blocks.keys()):
        for suffix in language_blocks[lang]:
            if rooturl.endswith(suffix):
                suffixlangs.append(lang)
    try:
        infixlangs = GetInfixLanguage(url)
    except InvalidLanguageException as e:
        # Don't care, we're just trying to identify the page.
        infixlangs = e.message
    # Next we extract what information we can from the HTML content.
    #langloc = html.find(u'lang=')
    #contentloc = html.find(u'content-language')
    soup = BeautifulSoup(html)
    html_lang = None
    content_lang = None
    try:
        html_lang = soup.findAll('html')[0].get('lang', None)
    except Exception:
        pass
    try:
        cl = soup.findAll(attrs={'http-equiv': 'Content-Language'})[0].get('content', None)
        content_lang = cl.get('content', None)
        print('Content Lang: {0} - {1}'.format(cl, content_lang))
    except Exception:
        pass
    if not content_lang:
        try:
            cl = soup.findAll(attrs={'name': 'language'})[0].get('content', None)
            content_lang = cl.get('content', None)
            print('Content Lang: {0} - {1}'.format(cl, content_lang))
        except Exception:
            pass
    #print(u'Infix langs: {0}, Suffix Langs: {1}, Prefix Lang: {2}, HTML Lang: {3}, Content Lang: {4}'.format(
    #    infixlangs, suffixlangs, prefix, html_lang, content_lang))
    if html_lang:
        return [html_lang]
    if content_lang:
        return [content_lang]
    if infixlangs:
        return [infixlangs]
    if suffixlangs:
        return suffixlangs
    if prefix:
        return [prefix]
    return []

def GetLanguageFromDomainExtension(rooturl):
    try:
        suffix = GetDomainExtension(rooturl)
        extension = DomainSuffix.objects.get(extension=suffix)
        if extension.default_language:
            return extension.default_language
        else:
            return None
    except ObjectDoesNotExist:
        pass
    return None

# To get corpus, and others.
# import nltk
# nltk.download()
# Get: langid, punkt, stopwords
#
# To get the full set of stopwords working, do this:
# cp dir/stopwords/* /home/jchampion/nltk_data/corpora/stopwords/
def NLTKLanguageDetect(text):
    # Uncomment to see which languages are available.
    # print stopwords.fileids()
    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]
    languages_ratios = {}
    for language in stopwords.fileids():
        try:
            stopwords_set = set(stopwords.words(language))
        except UnicodeDecodeError:
            print('UnicodeDecodeError getting stopwords for language {0}. Cannot categorize that language.'.format(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)
        languages_ratios[language] = len(common_elements)
    # print languages_ratios
    most_rated_language = max(languages_ratios, key=languages_ratios.get)
    # print most_rated_language
    return most_rated_language

def IdentifyLanguage(text):
    return identifier.classify(text)
