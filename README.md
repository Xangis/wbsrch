# WbSrch

The WbSrch search engine.

This is the source code used for the WbSrch search engine, which ran from fall 2013 until summer
2016. At the time it was shut down, it had about 54 million pages in 14 languages.

It is designed around the use of Django and PostgreSQL, not because they're a good choice for the
task, but because I wanted to see how far I could take them. Fairly far, it turns out.

Though some work may be done to keep it up to date and/or improve documentation, this should be
considered abandonware.

# Setup

Linux is required. It doesn't matter which version, but it has only been tested with Ubuntu Server.

WbSrch requires PostgreSQL. The version doesn't matter as long as it's 9.x or higher. If you don't
have it yet, install it with:

sudo apt-get install postgresql-client-9.5 postgresql-9.5 libpq-dev

(or whatever version your Linux distro has available)

Postgresql should be set up for local password authentication rather than peer. If that doesn't mean
anything to you, look up what the pg_hba.conf file is and how to configure it.

Redis is used for cache. It's not strictly required -- without it, there will be no caching and 
the user experience will run much slower. You should install it with:

sudo apt-get install redis-server

Create a python virtual environment. I like virtualenvwrapper, which lets you do something like:

mkvirtualenv wbsrch

Then, install the requirements. Note that python-dev, libgeoip-dev and libpq-dev have to be 
installed for the requirements.txt to grab everything correctly.

pip install -r requirements.txt

# Other Prerequisites

The system uses the MaxMind data for GeoIP. geoip_update.sh must be run at least once to get this data.
It should be run periodically to refresh the GeoIP data.

The system also use NLTK and needs to download module for it and install additional stopwords files.
Run nltk_download.sh to do that (be sure your virtualenv is active).

# Database

WbSrch requires 4 PostgreSQL databases. They can be on the same server, or on different servers. They are:

urls - Tracks the URLs to be crawled and the page-to-page links.

indexes - Contains the compiled indexes and search logs. This is for the user-facing search website.

zetaweb - Contains the page data.

news - For news site crawling. Not fully implemented.

Database configuration is stored in zetaweb/settings.py. Once you've created the databases, update that
file with username and password information.

When that's done you can run "python manage.py migrate" in the root of the application directory
(with your virtual environment activated, of course). You have to run this once for each database, like so:

python manage.py migrate
python manage.py migrate --database indexes
python manage.py migrate --database urls

You should absolutely not use the default settings on Postgres because they don't take advange of enough
RAM. The pgtune utility does a good job of choosing initial settings. The important thing is giving it
enough buffers and working memory to perform large operations.

Django's model system does not create all of the indexes required to make everything run efficiently. With
PostgreSQL that means GIN indexes. They make a massive difference in performance when computing index terms.
They'll slow down inserts a little, and therefore result in slower page crawling (but not much), but the
speed improvement for indexing is anywhere from 2x to 100x depending on the text (usually about 20x). There
is not an SQL script to do this yet, so you'll have to do so manually. EXPLAIN ANALYZE is your friend. And,
to get the search engine to use the indexes, you'll probably have to set random page cost low in the psql
config file.

# Deployment

There are a few things to be done when the site is deployed.

- Minify the Javascript: Run ./minifyjs.sh to minify JavaScript code. Requires uglifyjs. If you don't
have it, sudo apt-get install node-uglify.

- Minify the CSS: Run ./minifycss.sh to minify CSS files.

- Compile language translations: Run ./languages.sh to compile language translations.

# Crawling and Indexing

Everything runs based on daemons. The crawler and indexer daemons are most important, and any number
of daemons can run. It should depend on how much RAM, how many processor cores, and how much disk
space the system has.

One common option for seeding the initial crawl is the Alexa top 1 million sites. There is a script,
alexa_import, that will do that. Be warned, though, that it's easy to game the Alexa rankings, so
there is a LOT of spam, especially in the bottom half. There are also a lot of the type of thing
that ad networks won't let you place ads against -- porn, gambling, actual nazis, pill spam, malware,
etc.

When building the initial index, it may be helpful to use the language word lists in the /wordlists 
folder. You can queue up a dictioary of words with:

python manage.py add_new_to_pending -l tr -f wordlists/tr.txt.csv -m 2000000

This will add all of the words in the tr.txt.csv file to the pending index table, which you can then
index with the "python manage.py index" command. Note that you have to have some pages crawled, or
nothing will be indexed.

The system was originally designed with three different machines - a crawler, an indexer, and a web
server. The crawler ran on the same system as the urls database, the indexer on the same system as
the "zetaweb" page database, and the web server runs on the same system as the indexes. All three of
these databases can run on a single machine without any trouble.

A rule of thumb (at least for low-end dedicated servers) is to have 4 crawlers per core or one indexer
per core. Adjusting the "sleep time" between pages or index terms can be used for reducing load.

One of the hardest problems with this search engine is keeping the indexes up to date as new pages are
crawled. Since everything is based on computed indexes, a newly crawled page can take a long time to
show up in all of the indexes where it would be ranked. It depends on how quickly the indexes are recomputed
with the index_daemon or "python manage.py index".

Other daemons, the domain_update, domain_data_update, robots_update, and recrawl_daemon may or may not
be necessary (a lot of things exist to update existing data, which you may or may not want to do). Some
things, like the robots daemon, exist to update data that wasn't originally collected, but is now.

# Language Categorization

The engine does not analyze page language at crawl-time. That's a semi-manual process handled by the
categorize_language admin command. To auto-tag page languages that the detector finds with high confidence,
run a command something like this:

python manage.py categorize_language -o -c -a en,de,es,it,fr,pt,pl,sv,fi,nl,cs,el,hu,tr -i 9999

Other variants let you manually review sites. This is complicated, because there are many multilinguals sites
and many of them use different methods of language switching. The more pages you have from a site, the better
that language classification will be.

To block and remove sites/pages in languages you don't want to index, a command like this can be used:

python manage.py categorize_language -o -c -b id,zh,ru,ar,bg,ja,ko,vi,lt,lv,ta,he -i 9999

The meta content-language and html lang tags are NOT reliable for the web. Many frameworks default to
lang="en", while others have content-language default settings that users never change. Webites exist that
have lang="en", content-language="es" and are actually in catalan.

In addition, multilingual sites use many schemes, including subdomains, subdirectories, etc. All of these are
common:

http://de.example.com/page.htm
http://example.com/de/page.htm
http://example.com/de-de/page.htm
http://example.com/page.htm?lang=de
http://example.com/page.htm?hl=de_de
http://example.com/page_de.htm
http://de.example.com/page.htm?lang=en-us

Some, but not all of these, are obvious and easy to detect.

# Maintenance

This is a very high-maintenance search engine.

- Domain Links

The python manage.py domain_link_update command needs to run in order for incoming links to a domain to be counted.
This will influence how well that site ranks. Typically this is run as a daemon via python domain_link_daemon.py

- Index Stats

The index stats page is fairly database intensive, since it has to count page and index totals for all languages.
Python manage.py generate_index_stats will create a static version of that page. You should run it daily, weekly, or
monthly depending on how much your index changes.

- Vacuuming

Vacuuming the database can get to be problematic and time-consuming if you have a large index. But it will need to be
done on occasion because the indexer will stop using the indexes if you don't. Increasing the pg stats target in
the Postgres config will help with index use.

# Conclusion

You should absolutely not use the WbSrch engine if you want to build a full-sized consumer-facing search engine.
If you want to build something like the late-1990's search engines (AltaVista, Infoseek, or early Google), then
it'll be a good choice.

On a reasonably powerful machine (20 cores, 256GB of RAM, and 2TB or more of RAID 10 SSD storage), this engine performs
fairly well up to at least 50 million pages indexed. IF you add the database indexes mentioned above. It hasn't been
tested beyond that point.

If you're crawling the entire web, you need billions of pages, not just tens of millions. Yes, most pages are duplicates,
spam, content-free placeholder pages, or auto-generated fluff, but even if you prune all of that stuff out, there's
still far too much to handle.

This is a better choice if you just want to play around with crawling and indexing pages for your own learning and 
amusement.
