This folder contains config files used with WbSrch.

blockips.conf
  IP block list. Goes in /etc/nginx/

certbot.txt
  Info on setting up SSL certificates using Certbot.

createdb.sql
  SQL commands to create all required databases, user, and permissions. You will want to
  choose a different password and enter that into zetaweb/settings.py.

django-wbsrch
  init.d script, goes in /etc/init.d/, not used anymore, but may be useful reference.

fastcgi.conf
  NGINX FastCGI config file, goes in /etc/nginx/

nginx.conf
  NGINX config file, goes in /etc/nginx/

packages.sh
  One-off shell script to install all of the Ubuntu packages that WbSrch depends on.

pg_hba.conf
  Postgresql authentication configuration. The default configuration doesn't allow password access
  or remote access.

postgresql.conf.*
  These configs are various versions for different servers. Postgresql doesn't allow remote connections
  by default and it doesn't take advantage of high amounts of RAM or fast disks. These configs address
  those.

uwsgi.wbsrch.conf
  uWSGI configuration file, goes in init.d. Used to start and stop the WbSrch service on an
  Upstart-based system.

uwsgi.wbsrch.service
  uWSGI configuration file for running on a systemd-based system. Goes in the
  /etc/systemd/system/ folder.

wbsrch.com
  Web config file for nginx. Goes in /etc/init.d/sites-available with a symbolic link in
  ../sites-enabled.

wbsrch_cron
  Cron job file, goes in /etc/cron.d/, runs daiy tasks like the index stats generation

packages.sh
  Used for installing apt packages required by WbSrch in all one go.
