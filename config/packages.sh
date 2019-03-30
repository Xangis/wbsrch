sudo apt-get remove apache2
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install certbot build-essential nginx python2.7-dev postgresql-client-10 postgresql-10 libpq-dev redis-server gettext node-uglify \
 python-virtualenv virtualenvwrapper libgeoip-dev dnsutils libpqxx-dev lm-sensors unzip usbmount uwsgi uwsgi-plugin-python zip exim4
