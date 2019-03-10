=====
Usage
=====

To use API clients permission. in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'api_clients.apps.ApiClientsConfig',
        ...
    )

Add API clients permission.'s URL patterns:

.. code-block:: python

    from api_clients import urls as api_clients_urls


    urlpatterns = [
        ...
        url(r'^', include(api_clients_urls)),
        ...
    ]
