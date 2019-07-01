##########
PySunsetWx
##########
|Latest Version| |Say Thanks|

A simple and open source Python wrapper for the `SunsetWx <https://sunsetwx.com/>`_ `Sunburst REST API <https://sunburst.sunsetwx.com/v1/docs/>`_,
which provides sunset and sunrise quality forecasts.

The source code is available on GitHub at `https://github.com/salvoventura/pysunsetwx <https://github.com/salvoventura/pysunsetwx>`_.

.. note::  When using this library you need to abide to SunsetWx Guidelines, which are explained on `SunsetWx API page <https://sunburst.sunsetwx.com/v1/docs/#introduction>`_


############
Installation
############
``PySunsetWx`` is available on `PyPI <https://pypi.python.org/pypi>`_ and thus can be installed with ``pip`` on most platforms.
::

    $ pip install pysunsetwx

############
Dependencies
############
This library depends on `Requests <http://docs.python-requests.org>`_ to make - well - requests to the SunsetWx API.
This additional package should be automatically installed at installation time, or you can simply install it by:
::

    $ pip install requests

#####
Usage
#####
Before you can interact with the SunsetWx Sunburst API, you need to register your email address and password. You
can do that by registering an account at `https://subscriptions.sunsetwx.com/register <https://subscriptions.sunsetwx.com/register>`_.
You can use your email/password from registration for the API calls.

.. note:: At time of writing, there is no need to select a subscription nor to insert any payment information, as long as you abide to SunsetWx Guidelines, which are explained on `SunsetWx API page <https://sunburst.sunsetwx.com/v1/docs/#introduction>`_


Constructor
===========
Creates a new API object with your email and password. Automatically handles login, authentication, and auth token refresh.

::

    from pysunsetwx import PySunsetWx
    py_sunsetwx = PySunsetWx('yourname@example.org', 'Your1Password')

-
    **Parameters**

    ============  ======  ========================  =====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  =====================================
    username      str     Required                  Used when registering to the service
    password      str     Required                  Used when registering to the service
    ============  ======  ========================  =====================================

    **Returns**

    ==========  =======================================
    **object**  ``PySunsetWx`` class instance
    ==========  =======================================


.get_quality(latitude, longitude, event)
========================================
Returns an array of points, within range of the given coordinates, that contains quality predictions for the next
sunrise or sunset.

::

    from pysunsetwx import PySunsetWx
    py_sunsetwx = PySunsetWx('yourname@example.org', 'Your1Password')
    quality = py_sunsetwx.get_quality(37.773972, -122.431297, 'sunset')

-
    **Parameters**

    ============  ======  ========================  =====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  =====================================
    latitude      float   Required                  Latitude of location of interest
    longitude     float   Required                  Longitude of location of interest
    event         str     Optional                  'sunset', 'sunrise', default=None
                                                    for next-occurring event type
    ============  ======  ========================  =====================================

    **Returns**

    ==========  =======================================
    **dict**    JSON data from API call data to dict
    ==========  =======================================


########
Examples
########
This example shows how to login and retrieve sunset quality data for San Francisco. Other examples in the library
`examples` folder.

.. code-block:: python

        import os
        from pysunsetwx import PySunsetWx
        username = os.environ.get('USERNAME', None) or 'USERNAME'
        password = os.environ.get('PASSWORD', None) or 'PASSWORD'

        # instantiate PyPexels object
        py_sunsetwx = PySunsetWx(username, password)

        # get Quality values for San Francisco (37.773972, -122.431297)
        quality = py_sunsetwx.get_quality(37.773972, -122.431297, 'sunset')

        # print them out
        print(quality)

        # OUTPUT:
        # {
        #    'type':'FeatureCollection',
        #    'features':[
        #       {
        #          'type':'Feature',
        #          'geometry':{
        #             'type':'Point',
        #             'coordinates':[
        #                -122.429,
        #                37.777
        #             ]
        #          },
        #          'properties':{
        #             'type':'Sunset',
        #             'quality':'Fair',
        #             'quality_percent':37.51,
        #             'quality_value':-147.696,
        #             'temperature':12.73,
        #             'last_updated':'2019-06-30T12:00:00Z',
        #             'imported_at':'2019-06-30T15:33:11Z',
        #             'valid_at':'2019-07-01T03:36:00Z',
        #             'dusk':{
        #                'civil':'2019-07-01T04:07:00Z',
        #                'nautical':'2019-07-01T04:46:00Z',
        #                'astronomical':'2019-07-01T05:30:00Z'
        #             },
        #             'source':'NAM',
        #             'distance':0.393
        #          }
        #       }
        #    ]
        # }



#######
Version
#######
**PySunsetWx v1.0.0b1 (beta, v1)**

    First release of the PySunsetWx library.

    .. note::  When using this library you still need to abide to SunsetWx Guidelines, which are explained on `SunsetWx API page <https://sunburst.sunsetwx.com/v1/docs/#introduction>`_


#######
License
#######
PySunsetWx is released under the `MIT License <http://www.opensource.org/licenses/MIT>`_.


.. |Latest Version| image:: https://badge.fury.io/py/pysunsetwx.svg
    :target: https://badge.fury.io/py/pysunsetwx

.. |Say Thanks| image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
   :target: https://saythanks.io/to/salvoventura
   :alt: Say Thanks
