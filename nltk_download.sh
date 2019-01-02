#!/bin/bash
mkdir -p ~/nltk_data/corpora/stopwords/
python -m nltk.downloader punkt
python -m nltk.downloader stopwords
cd dir/stopwords;./copy.sh
