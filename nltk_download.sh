#!/bin/bash
python -m nltk.downloader punkt
python -m nltk.downloader stopwords
cd dir/stopwords;./copy.sh
