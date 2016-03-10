#!/bin/bash
# This script installs server prerequisites and config files.
# The intent is to have a working server after this script has been run.
# We are not there yet.
echo Installing apt packages.
sudo apt-get install lm-sensors python python-virtualenv virtualenvwrapper libpq-dev python-dev postgresql-9.3-postgis-2.1 git zip unzip bind9 bind9utils openssh-server nginx build-essential usbmount memcached aptitude sysstat pgtune automake libtool gdb
echo Copying NGINX config.
sudo cp wbsrch.com /etc/nginx/sites-available/wbsrch.com
echo Linking NGINX config.
sudo ln -s /etc/nginx/sites-available/wbsrch.com /etc/nginx/sites-enabled/wbsrch.com
echo Copying NGINX IP block list.
sudo cp blockips.conf /etc/nginx/blockips.conf
echo Testing NGINX config.
sudo nginx -t
echo Copying WSGI config.
sudo cp uwsgi.wbsrch.conf /etc/init/uwsgi.wbsrch.conf
echo Copying /etc/evironment.
sudo cp etc.environment /etc/environment
echo Copying SSH certificates.
sudo mkdir -p /etc/nginx/certs
sudo cp wbsrch.crt wbsrch.key /etc/nginx/certs/
echo Setting up cron job.
sudo cp wbsrch_cron /etc/cron.d/wbsrch_cron
echo Setting up virtualenv.
mkvirtualenv wb
workon wb
pip install -r ../requirements.txt
