###############################################################################
#    Copyright (c) 2019 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: errors.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 6/29/2019
#   Purpose: 
#            
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################


class SunsetWxError(Exception):
    def __init__(self, message):
        self.message = str(message) if message else "Unknown error"
        super(SunsetWxError, self).__init__(message)

    def __str__(self):
        return self.message
