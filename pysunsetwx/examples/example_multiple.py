###############################################################################
#    Copyright (c) 2019 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: test.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 6/30/2019
#   Purpose: Example checking multiple cities with single login.
#            We prefer to import credentials through OS Environment variables
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
from __future__ import print_function

import os

from pysunsetwx import PySunsetWx

username = os.environ.get('USERNAME', None) or 'USERNAME'
password = os.environ.get('PASSWORD', None) or 'PASSWORD'

cities = [
    ('San Francisco, USA', (37.432335, -121.899574)),
    ('Rome, Italy', (41.89193, 12.51133)),
    ('Sydney, Australia', (-33.865143, 151.209900)),
]

# Instantiate the PySunsetWx class
py_sunsetwx = PySunsetWx(username, password)

# Iterate through the cities list
for city, coords in cities:
    print('Checking quality for %s' % city)
    quality = py_sunsetwx.get_quality(*coords)
    elem = quality['features'][0]['properties']
    print('%s quality is %s' % (elem['type'], elem['quality']))
    print('\n\n')
