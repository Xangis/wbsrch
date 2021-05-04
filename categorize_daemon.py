from subprocess import call
from multiprocessing import Pool
import argparse


parser = argparse.ArgumentParser(description="Categorize language by extension, multiprocess version.")
parser.add_argument('extensions', default=None, action='store', type=str, dest='extensions', help='Comma-separated list of extensions to process.')
parser.add_argument('-p', '--processes', default=4, action='store', type=int, dest='processes', help='Number of concurrent processes for categorization (default=4).')
options = parser.parse_args()


# Block, then categorize, then tag English.
def ProcessExtension(extension):
    print('Processing extension {0}'.format(extension))
    call(['python', 'manage.py', 'categorize_language', '-c', '-t', '-b', 'am,ar,as,az,be,bg,bn,cn,dz,fa,gu,he,hi,hy,id,ja,jv,ka,kk,km,kn,ko,ku,ky,lo,mk,ml,mn,mr,ms,ne,or,pa,ps,ru,si,sq,sr,ta,te,th,tl,ug,uk,ur,vi,zh', '-q', '-i', '10000000', '-u', '.{0}'.format(extension)])
    call(['python', 'manage.py', 'categorize_language', '-c', '-t', '-a', 'an,ca,cs,cy,da,de,el,es,et,eu,fi,fr,gl,hr,hu,is,it,lt,lv,nl,no,pl,pt,ro,rw,sl,sv,sw,tr,rw,xh,zu', '-q', '-o', '-j', '-i', '10000000', '-u', '.{0}'.format(extension)])
    call(['python', 'manage.py', 'categorize_language', '-e', '-o', '-t', '-q', '-n', '3', '-i', '10000000', '-u', '.{0}'.format(extension)])
    print('Done processing extension {0}'.format(extensions))


# These are the extensions found in a 3 million URL crawl ordered from least common to most.
extensions = ['abb', 'scb', 'whoswho', 'new', 'mango', 'nra', 'softbank', 'autos', 'rmit', 'cancerresearch',
'kpmg', 'sap', 'dvag', 'abarth', 'aeg', 'amica', 'arte', 'azure', 'bauhaus', 'bbva', 'bing', 'bms', 'bom',
'bond', 'bridgestone', 'budapest', 'caravan', 'cartier', 'cbn', 'ceb', 'cfd', 'chanel', 'cipriani', 'dabur',
'datsun', 'delta', 'epson', 'eurovision', 'everbank', 'final', 'firmdale', 'genting', 'ggee', 'giving',
'gmo', 'goldpoint', 'goo', 'goodyear', 'hitachi', 'hotmail', 'hyundai', 'icbc', 'infiniti', 'kddi', 'kia',
'lancaster', 'lixil', 'lupin', 'man', 'microsoft', 'nadex', 'nec', 'nhk', 'nico', 'office', 'omega', 'otsuka',
'pay', 'philips', 'piaget', 'ping', 'sakura', 'sanofi', 'sca', 'scholarships', 'schwarz', 'scor', 'seven',
'sew', 'skype', 'spreadbetting', 'stada', 'stcgroup', 'suzuki', 'swatch', 'tui', 'uol', 'virgin', 'vistaprint',
'viva', 'walter', 'watches', 'windows', 'wme', 'wtc', 'xbox', 'xn--cck2b3b', 'xn--estv75g', 'xn--kcrx77d1x4a',
'xn--vermgensberater-ctb', 'xn--vermgensberatung-pwb', 'yodobashi', 'zuerich', 'smart', 'select', 'clubmed',
'cfa', 'ismaili', 'kyoto', 'tiaa', 'volvo', 'extraspace', 'fast', 'homesense', 'lpl', 'mint', 'pars', 'total',
'weir', 'rwe', 'locus', 'trust', 'abc', 'aramco', 'audible', 'imdb', 'ipiranga', 'kindle', 'lexus', 'seek',
'silk', 'sky', 'toshiba', 'xn--mgba3a3ejt', 'yamaxun', 'zappos', 'creditunion', 'hsbc', 'bugatti', 'xn--55qx5d',
'xn--o3cw4h', 'xn--90ae', 'xn--l1acc', 'xn--vuq861b', 'xn--zfr164b', 'xn--p1ai', 'xn--kput3i', 'xn--h2brj9c',
'xn--wgbl6a', 'xn--j6w193g', 'xn--mgbaam7a8h', 'xn--kpry57d', 'xn--czr694b', 'aaa', 'qpon', 'bmw', 'tatar',
'maif', 'ikano', 'citic', 'stockholm', 'stc', 'sncf', 'boats', 'er', 'sbi', 'dnp', 'axa', 'brother',
'hisamitsu', 'honda', 'yandex', 'nissan', 'crown', 'luxe', 'itau', 'gw', 'globo', 'fox', 'sharp', 'fire', 'jll',
'sony', 'storage', 'tatamotors', 'ice', 'toyota', 'pictet', 'xn--90ais', 'goog', 'barclaycard', 'ses',
'auspost', 'schmidt', 'aquarelle', 'dhl', 'erni', 'cyou', 'gn', 'kp', 'ricoh', 'monash', 'jcb', 'saxo', 'toray',
'williamhill', 'charity', 'aws', 'leclerc', 'aco', 'rugby', 'barclays', 'kred', 'abudhabi', 'gf', 'komatsu',
'kr', 'rich', 'xn--nyqy26a', 'sener', 'xn--90a3ac', 'corsica', 'baby', 'observer', 'lidl', 'fage', 'hospital',
'xn--j1amh', 'xn--c1avg', 'cooking', 'wed', 'theatre', 'sandvik', 'google', 'mq', 'lamborghini', 'td', 'weber',
'organic', 'mom', 'afl', 'forex', 'audi', 'neustar', 'boston', 'monster', 'bnpparibas', 'post', 'fan', 'nr',
'vodka', 'canon', 'inc', 'protection', 'cpa', 'ren', 'shriram', 'insurance', 'rodeo', 'km', 'gu', 'cern', 'ong',
'seat', 'fk', 'realty', 'fishing', 'ruhr', 'xn--80adxhks', 'reit', 'sport', 'ne', 'basketball', 'bradesco',
'cab', 'pharmacy', 'shopping', 'vlaanderen', 'lgbt', 'poker', 'alsace', 'abbott', 'cg', 'homes', 'xn--3e0b707e',
'ceo', 'realestate', 'xn--mgbab2bd', 'xn--hxt814e', 'ltda', 'bot', '20', 'mr', 'security', 'kn', 'llc', 'salon',
'voto', 'xn--tckwe', 'crs', 'aq', 'krd', 'casa', 'broker', 'radio', 'barcelona', 'promo', 'nrw', 'istanbul',
'physio', 'tg', 'surf', 'car', 'bj', 'bayern', 'cars', 'pn', 'wf', 'miami', 'abogado', 'taipei', 'tube', 'bf',
'gdn', 'koeln', 'game', 'xn--fiqs8s', 'cam', 'va', 'xn--p1acf', 'mp', 'hm', 'page', 'markets', 'lr', 'country',
'trading', 'bible', 'tirol', 'hamburg', 'menu', 'ye', 'auto', 'sb', 'ist', 'ki', 'ryukyu', 'airforce', 'cw',
'xn--80aswg', 'dm', 'sy', 'osaka', 'moscow', 'ck', 'gop', 'yt', 'pf', 'bs', 'hiv', 'realtor', 'onl', 'feedback',
'green', 'sm', 'vi', 'brussels', 'tm', 'memorial', 'bi', 'tf', 'rio', 'horse', 'sx', 'ax', 'melbourne', 'degree',
'sl', 'shiksha', 'ad', 'ls', 'iq', 'gmbh', 'museum', 'eco', 'ht', 'xn--6frz82g', 'cv', 'sarl', 'pr', 'aw', 'gp',
'cd', 'republican', 'doctor', 'gm', 'navy', 'best', 'xn--80asehdb', 'sz', 'sr', 'juegos', 'bn', 'ngo', 'sd',
'build', 'bzh', 'mg', 'beer', 'maison', 'xn--q9jyb4c', 'study', 'tickets', 'reise', 'pm', 'lc', 'mm', 'luxury',
'tires', 'mw', 'democrat', 'ni', 'et', 'dj', 'hockey', 'viajes', 'ao', 'bet', 'creditcard', 'webcam', 'courses',
'sn', 'nf', 'bb', 'bingo', 'bt', 'ci', 'theater', 'army', 'mc', 'hiphop', 'gives', 'mo', 'lat', 'fans', 'health',
'desi', 'hn', 'mz', 'africa', 'gy', 'movie', 'pg', 'soy', 'fj', 'gi', 'gripe', 'jm', 'gd', 'bank', 'gent', 'bw',
'games', 'sv', 'tennis', 'rest', 'kg', 'om', 'so', 'blackfriday', 'zm', 'cricket', 'vote', 'faith', 'ooo',
'accountant', 'gal', 'fish', 'rw', 'stream', 'bh', 'mv', 'guitars', 'racing', 'garden', 'lease', 'schule',
'gs', 'tt', 'nc', 'cologne', 'rehab', 'accountants', 'gl', 'archi', 'vip', 'je', 'kw', 'actor', 'coupons',
'limited', 'tienda', 'art', 'cu', 'christmas', 'film', 'claims', 'flowers', 'moda', 'af', 'rip', 'mba', 'moe',
'how', 'tattoo', 'rent', 'irish', 'engineer', 'cm', 'kh', 'py', 'soccer', 'ltd', 'diet', 'villas', 'na', 'bid',
'ac', 'flights', 'int', 'saarland', 'vu', 'dz', 'quebec', 'download', 'futbol', 'cleaning', 'gh', 'jewelry',
'furniture', 'credit', 'durban', 'trade', 'ky', 'jetzt', 'do', 'uz', 'cx', 'bargains', 'bo', 'delivery', 'srl',
'surgery', 're', 'mortgage', 'pet', 'dev', 'fun', 'ms', 'lb', 'auction', 'okinawa', 'supplies', 'associates',
'eus', 'pa', 'men', 'gold', 'exposed', 'gifts', 'condos', 'ps', 'zw', 'florist', 'work', 'limo', 'bm', 'voyage',
'host', 'dating', 'industries', 'reisen', 'taxi', 'hosting', 'tn', 'ag', 'fail', 'qa', 'wien', 'joburg', 'jo',
'group', 'cr', 'loans', 'investments', 'dentist', 'cheap', 'cruises', 'diamonds', 'discount', 'mil', 'casino',
'haus', 'sh', 'catering', 'gratis', 'fo', 'black', 'vin', 'apartments', 'ug', 'town', 'gt', 'buzz', 'financial',
'express', 'sc', 'review', 'yokohama', 'kiwi', 'mu', 'pink', 'tc', 'place', 'bd', 'cy', 'toys', 'glass', 'vc',
'pizza', 'insure', 'college', 'show', 'mn', 'vg', 'eg', 'date', 'builders', 'recipes', 'bar', 'cards', 'earth',
'supply', 'ski', 'st', 'engineering', 'gift', 'computer', 'contractors', 'camera', 'law', 'vacations', 'uno',
'property', 'wedding', 'as', 'report', 'by', 'plumbing', 'az', 'restaurant', 'store', 'singles', 'capetown',
'nagoya', 'al', 'dance', 'mk', 'holdings', 'productions', 'vet', 'football', 'university', 'shoes', 'holiday',
'np', 'mt', 'watch', 'parts', 'kz', 'fund', 'golf', 'partners', 'style', 'vision', 'blog', 'tz', 'sale',
'enterprises', 'plus', 'finance', 'ec', 'lol', 'camp', 'gq', 'clinic', 'run', 'immobilien', 'fashion', 'global',
'ma', 'audio', 'gg', 'shop', 'tours', 'forsale', 'exchange', 'tax', 've', 'boutique', 'app', 'domains', 'li',
'market', 'energy', 'kitchen', 'dog', 'ly', 'equipment', 'lighting', 'band', 'cash', 'cymru', 'kaufen', 'repair',
'chat', 'dental', 'press', 'kim', 'swiss', 'healthcare', 'ba', 'fyi', 'im', 'travel', 'cafe', 'solar', 'coach',
'pictures', 'pics', 'careers', 'deals', 'immo', 'construction', 'team', 'graphics', 'md', 'fit', 'aero', 'capital',
'sexy', 'fitness', 'money', 'sydney', 'love', 'yoga', 'family', 'uy', 'ink', 'school', 'foundation', 'top',
'tools', 'la', 'wine', 'wtf', 'sucks', 'help', 'coop', 'codes', 'blue', 'ge', 'community', 'software', 'institute',
'estate', 'email', 'attorney', 'sex', 'loan', 'legal', 'wiki', 'ventures', 'direct', 'management', 'video',
'business', 'am', 'ai', 'cool', 'ml', 'icu', 'cf', 'clothing', 'farm', 'vegas', 'xxx', 'bg', 'coffee', 'studio',
'properties', 'rentals', 'social', 'sa', 'ke', 'works', 'ga', 'bz', 'bio', 'pub', 'adult', 'pe', 'lawyer', 'scot',
'science', 'bike', 'to', 'care', 'wales', 'lk', 'land', 'is', 'porn', 'guide', 'party', 'house', 'photo', 'reviews',
'tl', 'support', 'zone', 'gallery', 'training', 'directory', 'ng', 'marketing', 'xin', 'wang', 'click', 'digital',
'consulting', 'rs', 'education', 'live', 'city', 'academy', 'international', 'photos', 'lu', 'events', 'network',
'church', 'cat', 'jobs', 'paris', 'lv', 'si', 'hr', 'systems', 'red', 'tel', 'ovh', 'center', 'london', 'frl', 'pw',
'ee', 'technology', 'services', 'fm', 'berlin', 'media', 'agency', 'design', 'expert', 'ae', 'photography', 'th',
'ph', 'tips', 'win', 'cloud', 'link', 'world', 'su', 'ninja', 'nu', 'tokyo', 'pk', 'amsterdam', 'id', 'news',
'life', 'company', 'one', 'lt', 'nyc', 'today', 'tech', 'solutions', 'hk', 'space', 'guru', 'rocks', 'website',
'name', 'site', 'gov', 'ua', 'vn', 'il', 'fi', 'cc', 'tk', 'ir', 'pt', 'cl', 'online', 'xn--p1ai', 'pro', 'tr',
'asia', 'sg', 'tw', 'cn', 'se', 'club', 'xyz', 'gr', 'my', 'ar', 'io', 'ro', 'cz', 'hu', 'pl', 'fr', 'ru', 'at',
'ie', 'es', 'kr', 'no', 'edu', 'mx', 'mobi', 'jp', 'dk', 'ws', 'br', 'tv', 'nl', 'eu', 'sk', 'it', 'me', 'nz',
'ch', 'za', 'co', 'be', 'de', 'in', 'us', 'ca', 'info', 'au', 'biz', 'uk', 'org', 'net', 'com']

extensions = [
# Not processed yet, but running in another thread
# 'co', 'cz', 'dk', 'es', 'eu', 'fr', 'it', 'nl',
# 'pl', 'ro', 'sk', 'za', 'uk', 'us', 'au', 'ca', 'de'
# Languages that are NOT done after they've been processed (redo in new run):
'br', 'ch', 'co', 'cz', 'dk', 'eu',
# Languages that are DONE after they've been processed:
'es', 'fr', 'it', 'nl', 'pl', 'ro', 'sk', 'za', 'uk',
'at', 'be', 'us', 'au', 'ca', 'de',
# ICANN extensions that are ready to process even though we haven't crawled the full files.
# Be sure to crawl these on the next ICANN crawl (all but .com are done crawling).
'app', 'bid', 'biz', 'buzz', 'club', 'dev', 'fun', 'icu', 'info', 'live', 'mobi', 'online',
'pro', 'rent', 'shop', 'site', 'space', 'store', 'tech', 'top', 'vip', 'website', 'work',
'xyz', 'org', 'net', 'com'
]


if __name__ == '__main__':
    files = []
    if options.extensions:
        extensions = options.extensions.split(',')
    else:
        pass
    print('Processing {0} extensions: \n{1}'.format(len(extensions), extensions))
    with Pool(options.processes) as p:
        p.map(ProcessExtension, extensions)
