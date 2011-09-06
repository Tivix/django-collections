.. _installation:

Installation
============
Download Django Collections
*********************

There are a couple ways for you to get Django-Collections,

    1. Clone the git repository `from GitHub <https://github.com/natgeo/django-collections>`_
    2. Use pip to install it from `PyPI <http://pypi.python.org/pypi/dynamic_collections>`_

::

	pip install dynamic_collections

Add Django Collections to your project
********************************

Add to INSTALLED_APPS

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dynamic_collections',
        ...
    )
    
Dependencies
************

Dependencies for this app usually depend on the backend's you choose to use.

For Haystack, you will need `Haystack`_\,  configured and installed in your app.

.. _Haystack: http://haystacksearch.org/


Continue with :ref:`getting_started` 
