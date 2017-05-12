# wbsrch
The WbSrch search engine.

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

The system uses the MaxMind data for GeoIP. geoip_update.sh must be run at least once to get this data.
It should be run periodically to refresh the GeoIP data.

The system also use NLTK and needs to download module for it and install additional stopwords files.
Run nltk_download.sh to do that (be sure your virtualenv is active).

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

The system was originally designed with three different machines - a crawler, an indexer, and a web
server. The crawler ran on the same system as the urls database, the indexer on the same system as
the "zetaweb" page database, and the web server runs on the same system as the indexes.

A rule of thumb (at least for older servers) is to have 4 crawlers per core or one indexer per core.

Other daemons, the domain_update, domain_data_update, robots_update, and recrawl_daemon may or may not
be necessary (a lot of things exist to update existing data, which you may or may not want to do). Some
things, like the robots daemon, exist to update data that wasn't originally collected, but is now.
