#!/bin/bash
# Runs tests with coverage for the project and outputs the report to coverage.txt
coverage run manage.py test
coverage report -m --omit='/usr/*' > coverage.txt
cat coverage.txt
