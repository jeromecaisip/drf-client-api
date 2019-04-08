=============================
API clients permission.
=============================

.. image:: https://badge.fury.io/py/api_clients.svg
    :target: https://badge.fury.io/py/api_clients

.. image:: https://travis-ci.org/jeromecaisip/api_clients.svg?branch=master
    :target: https://travis-ci.org/jeromecaisip/api_clients

.. image:: https://codecov.io/gh/jeromecaisip/api_clients/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/jeromecaisip/api_clients

API Key Permission Utility for Django Rest Framework


Quickstart
----------

Install API clients permission.::

    pip install api_clients

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'api_clients',
        ...
    )

Add API clients permission's permission class:

.. code-block:: python



    REST_FRAMEWORK = {
        ...
         'DEFAULT_PERMISSION_CLASSES': (
            'api_clients.permissions.HasAPIAccess',
          )
        ...
    }


Create a client model with the api key:

.. code-block:: python

    from api_client.models import Client
    client = Client.objects.create(api_key='my_api_key')


Include api key on the request headers:

.. code-block:: python

    headers = {'api-key: 'my_api_key'}



Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
