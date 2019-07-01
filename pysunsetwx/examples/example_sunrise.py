###############################################################################
#    Copyright (c) 2019 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: example_sunrise.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 6/30/2019
#   Purpose: Example for sunrise, and showcasing library custom logging
#            We prefer to import credentials through OS Environment variables
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
from __future__ import print_function

import logging
import os

from pysunsetwx import PySunsetWx

username = os.environ.get('USERNAME', None) or 'USERNAME'
password = os.environ.get('PASSWORD', None) or 'PASSWORD'


# Initialize app logging
logger = logging.getLogger()
logging.basicConfig(filename='app_example.log', level=logging.DEBUG)

# PySunsetWX logger defaults to level logging.ERROR
# If you need to change that, use getLogger/setLevel
# on the module logger, like this:
logging.getLogger(PySunsetWx.logger_name).setLevel(logging.DEBUG)

# add a headers to the log
logger.debug(80*'=')
logging.debug('Testing PySunsetWx')
logger.debug(80*'=')

# instantiate PyPexels object
py_sunsetwx = PySunsetWx(username, password)

# Get Sunrise Quality values for San Francisco (37.773972, -122.431297)
quality = py_sunsetwx.get_quality(37.773972, -122.431297, 'sunrise')

# print them out
print(quality)

# {
#     "type":"FeatureCollection",
#     "features":[
#         {
#             "type":"Feature",
#             "geometry":{
#                 "type":"Point",
#                 "coordinates":[
#                     -122.429,
#                     37.777
#                 ]
#             },
#             "properties":{
#                 "type":"Sunrise",
#                 "quality":"Good",
#                 "quality_percent":62.98,
#                 "quality_value":0.418624,
#                 "temperature":11.58,
#                 "last_updated":"2019-06-30T18:00:00Z",
#                 "imported_at":"2019-06-30T21:59:01Z",
#                 "dawn":{
#                     "astronomical":"2019-07-01T10:58:00Z",
#                     "nautical":"2019-07-01T11:42:00Z",
#                     "civil":"2019-07-01T12:21:00Z"
#                 },
#                 "valid_at":"2019-07-01T12:52:00Z",
#                 "source":"NAM",
#                 "distance":0.393
#             }
#         }
#     ]
# }
