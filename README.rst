Arcgis SDK
==========

|Pypi| |Wheel| |Build Status| |Codecov| |Code Climate|


Python SDK for Arcgis API


Installation
------------

Install from Pypi.

.. code:: sh

    pip install arcgis-sdk


Quick start
-----------

**Client**

.. code:: python

    >>> import arcgis_sdk
    >>> client = arcgis_sdk.ArcgisAPI('access_token')
    >>> client.self()


**Exceptions**

.. code:: python

    >>> try:
    ...     client.add_item(
    ...         username='mongkok',
    ...         title='my item',
    ...         type='Web Mapping Application'
    ...     )
    ... except arcgis_sdk.ArcgisAPIError as err:
    ...     print(err.message)


**Refresh the token**

.. code:: python

    >>> client.refresh_token('client_id', 'refresh_token')


Tests
-----

.. code:: sh

    make test


.. |Pypi| image:: https://img.shields.io/pypi/v/arcgis-sdk.svg
   :target: https://pypi.python.org/pypi/arcgis-sdk

.. |Wheel| image:: https://img.shields.io/pypi/wheel/arcgis-sdk.svg
   :target: https://pypi.python.org/pypi/arcgis-sdk

.. |Build Status| image:: https://travis-ci.org/mongkok/arcgis-sdk.svg?branch=master
   :target: https://travis-ci.org/mongkok/arcgis-sdk

.. |Codecov| image:: https://img.shields.io/codecov/c/github/mongkok/arcgis-sdk.svg
   :target: https://codecov.io/gh/mongkok/arcgis-sdk

.. |Code Climate| image:: https://codeclimate.com/github/mongkok/arcgis-sdk/badges/gpa.svg
   :target: https://codeclimate.com/github/mongkok/arcgis-sdk
