#!/bin/bash
# Requires node-uglify. If this fails, install that.
uglifyjs templates/wbsrch.js.orig --compress > templates/wbsrch.js
echo "wbsrch.js Original Size: "
wc templates/wbsrch.js.orig
echo "wbsrch.js Compressed Size: "
wc templates/wbsrch.js
