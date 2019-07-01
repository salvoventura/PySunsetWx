###############################################################################
#    Copyright (c) 2019 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: api.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 6/30/2019
#   Purpose: Base API class to provide basic REST functionalities, and auth
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
import time

import requests

from .errors import SunsetWxError
from .liblogging import logger
from .settings import API_VERSION, API_ROOT


class Api(object):
    def __init__(self, username, password, api_version=API_VERSION):
        self.username = username
        self.password = password
        self.api_version = api_version
        self.token_expiration = None
        self.access_token = None
        self._login()

    def _login(self):
        url = '/login'
        body = {
            'grant_type': 'password',
            'scope': ['predictions']
        }
        res = self.post(url, body)
        logger.debug('Login response=%s' % res)
        self.access_token = res.get('token')
        self.token_expiration = time.time() + res.get('token_exp_sec')

    def _validate_token(self):
        if self.token_expiration and (self.token_expiration - time.time() < 60):  # renew if less than a minute remaining
            logger.debug("Renewing authentication token")
            self._login()

    def _get_headers(self):
        headers = {
            'Content-Type': 'application/json',
        }
        if self.access_token:
            headers.update({
                'Authorization': 'Bearer %s' % self.access_token
            })
        logger.debug('Updated headers=%s' % headers)
        return headers

    def _request(self, method, url, data=None):
        """
        Perform an HTTP request. Automatically validates and renews auth token if necessary.
        :param method: POST or GET
        :param url: URI of the specific API endpoint after API_ROOT
        :param data: dictionary of data to pass in the request for POST requests
        :return:
        """
        full_url = API_ROOT + '/' + self.api_version + url
        self._validate_token()
        headers = self._get_headers()

        logger.debug('_request method=%s' % method.upper())
        logger.debug('_request url=%s' % full_url)
        logger.debug('_request headers=%s' % headers)
        logger.debug('_request data=%s' % data)

        if method.upper() == 'POST':
            r = requests.post(url=full_url, data=data, headers=headers, auth=(self.username, self.password))

        elif method.upper() == 'GET':
            r = requests.get(url=full_url, headers=headers)  # , auth=(self.username, self.password))

        else:
            msg = 'Method %s not supported' % method
            logger.debug(msg)
            raise SunsetWxError(msg)

        result = 'success' if r.status_code == 200 else 'failed'
        msg = '%s %s: %s %s' % (method.upper(), result, r.status_code, str(r.text))
        logger.debug(msg)

        if r.status_code != 200:
            raise SunsetWxError(msg)
        return r.json()

    def post(self, url, body):
        return self._request('POST', url, body)

    def get(self, url, params):
        expanded_params = '&'.join(["%s=%s" % (k, v) for k, v in params.items()])
        url = url + '?' + expanded_params
        logger.debug('get expanded url=%s' % url)
        return self._request('GET', url)




