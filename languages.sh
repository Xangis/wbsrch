#!/bin/bash
# Generates empty strings to be filled in for translations for all supported languages.
#
# When done, run python manage.py compilemessages.
#
# If this fails, make sure that the gettext system package is installed.
cd templates;python ../manage.py makemessages -a -e htm,inc;python ../manage.py compilemessages
