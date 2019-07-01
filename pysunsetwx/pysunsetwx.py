###############################################################################
#    Copyright (c) 2019 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: pysunsetwx.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 6/30/2019
#   Purpose: Main PySunsetWX class
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
from .src.api import Api
from .src.settings import LIB_NAME


class PySunsetWx(Api):
    logger_name = LIB_NAME

    def __init__(self, username, password):
        super(PySunsetWx, self).__init__(username, password)

    def get_quality(self, latitude, longitude, event=None):
        """
        Returns an array of points, within range of the given coordinates,
        that contains quality predictions for the next sunrise or sunset.

        :param latitude: float, latitude of location
        :param longitude: float, longitude of location
        :param event: str, 'sunrise' or 'sunset'. Default: None -> next-occurring event type
        :return: json response
        """
        url = '/quality'
        params = {'geo': '%s,%s' % (latitude, longitude), 'type': event}
        return self.get(url, params)





