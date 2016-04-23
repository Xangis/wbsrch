#!/bin/bash
# This script installs server prerequisites and config files.
# The intent is to have a working server after this script has been run.
# We are not there yet.
echo Installing apt packages.
sudo apt-get install lm-sensors python python-virtualenv virtualenvwrapper libpq-dev python-dev postgresql-9.3-postgis-2.1 git zip unzip bind9 bind9utils openssh-server nginx build-essential usbmount memcached aptitude sysstat pgtune automake libtool gdb uwsgi uwsgi-plugin-python libgeoip-dev gettext redis-server
echo Copying Postgres pg_hba.conf.
sudo cp pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf
sudo chown postgres:postgres /etc/postgresql/9.3/main/pg_hba.conf
echo Copying NGINX config.
sudo cp wbsrch.com /etc/nginx/sites-available/wbsrch.com
echo Linking NGINX config.
sudo ln -s /etc/nginx/sites-available/wbsrch.com /etc/nginx/sites-enabled/wbsrch.com
echo Copying NGINX IP block list.
sudo cp blockips.conf /etc/nginx/blockips.conf
echo Removing default NGINX config.
sudo rm /etc/nginx/sites-enabled/default
echo Testing NGINX config.
sudo nginx -t
echo Copying WSGI config.
sudo cp uwsgi.wbsrch.conf /etc/init/uwsgi.wbsrch.conf
echo Copying /etc/evironment.
sudo cp etc.environment /etc/environment
echo Copying SSH certificates.
sudo mkdir -p /etc/nginx/certs
sudo cp wbsrch.crt wbsrch.key /etc/nginx/certs/
echo Creating log directory
mkdir -p /var/django/wbsrch/log
echo Creating geoip directory
mkdir -p /var/django/wbsrch/geoip
echo Getting GeoIP Data Files
wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
wget http://download.maxmind.com/download/geoip/database/asnum/GeoIPASNum.dat.gz
gunzip GeoIPASNum.dat.gz
gunzip GeoIP.dat.gz
gunzip GeoLiteCity.dat.gz
mv GeoIPASNum.dat GeoIP.dat GeoLiteCity.dat geoip/
echo Setting up cron job.
sudo cp wbsrch_cron /etc/cron.d/wbsrch_cron
echo Setting up virtualenv.
mkvirtualenv wb
workon wb
pip install -r ../requirements.txt
