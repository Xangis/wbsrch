#!/bin/bash
python -m csscompressor templates/style.css.orig -o templates/style.css
echo 'Original Size:'
wc templates/style.css.orig
echo 'New Size:'
wc templates/style.css
