# A standalone utility to take a screenshot using Selenium and PhantomJS.
# This has been integrated into alexa_screenshots and/or elsewhere and is
# no longer needed. It is provided here for convenience of reuse.

import StringIO
from selenium import webdriver
from PIL import Image


# Install instructions
#
# npm install phantomjs
# sudo apt-get install libjpeg-dev
# pip install selenium pillow
WIDTH = 1280
HEIGHT = 800
SMALLWIDTH = 320
SMALLHEIGHT = 200

URL = 'analytics.wbsrch.com'

driver = webdriver.PhantomJS(executable_path="node_modules/phantomjs/bin/phantomjs")
driver.set_window_size(WIDTH, HEIGHT)  # optional
driver.get('https://{0}'.format(URL))
driver.save_screenshot('{0}.png'.format(URL))

screen = driver.get_screenshot_as_png()

# Crop it back to the window size (it may be taller)
box = (0, 0, WIDTH, HEIGHT)
im = Image.open(StringIO.StringIO(screen))
region = im.crop(box)
size = SMALLWIDTH, SMALLHEIGHT
region.thumbnail(size)
region.save('{0}.320px.png'.format(URL), 'PNG')
