#!/bin/bash
# Generates empty strings to be filled in for translations for all supported languages.
#
# When done, run python manage.py compilemessages.
cd templates;python ../manage.py makemessages -a -e htm,inc
