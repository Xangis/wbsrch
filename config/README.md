This folder contains config files used with WbSrch.

blockips.conf
  IP block list. Goes in /etc/nginx/

django-wbsrch
  init.d script, goes in /etc/init.d/

fastcgi.conf
  NGINX FastCGI config file, goes in /etc/nginx/

nginx.conf
  NGINX config file, goes in /etc/nginx/

wbsrch.com
  Web config file for nginx. Goes in /etc/init.d/sites-available with a symbolic link in
  ../sites-enabled.

wbsrch_cron
  Cron job file, goes in /etc/cron.d/, runs daiy tasks like the index stats generation
