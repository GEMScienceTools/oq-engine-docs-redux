.. _installing-the-openquake-engine:

Installing the OpenQuake Engine
===============================

Instructive YouTube video for the installation procedure:

.. youtube:: J46boursIRc
   :align: center

Hardware requirements
---------------------

The minimum required to install the engine and run the demos is

- 8 GB of RAM (16 GB on macOS Ventura)
- 4 GB of free disk space

To run any serious calculation (i.e. a model in GEM mosaic) you need at least 2 GB of RAM per thread for hazard 
calculations and even more memory for risk calculations. For instance, on a recent i9 processor with 32 threads you 
would need at least 64 GB of RAM.

Check more advanced `hardware suggestions here <https://github.com/gem/oq-engine/blob/master/doc/installing/hardware-suggestions.md>`_.

**WEBSITE NOT FOUND**

Installation Options
--------------------

Please follow the link in the dropdown menu depending on your operating system and version preferences.

.. dropdown:: Windows

    Dropdown content

.. dropdown:: MacOS

    Dropdown content

.. dropdown:: Linux

    Dropdown content

.. dropdown:: Advanced Options

    Dropdown content

Changing the OpenQuake Engine version
-------------------------------------

To change the version of the engine, make sure to uninstall the current version, before installing a new version.

- `Uninstalling the engine <https://github.com/gem/oq-engine/blob/master/doc/installing/universal.md#uninstalling-the-engine>`_
- `Installing a specific engine version <https://github.com/gem/oq-engine/blob/master/doc/installing/universal.md##installing-a-specific-engine-version>`_

Other installation methods
--------------------------

*************
Using ``pip``
*************

The OpenQuake Engine is also available on `PyPI <https://pypi.python.org/pypi/openquake.engine>`_ and can be installed in any Python 3 environment via ``pip``::

	```
	$ pip install -r https://raw.githubusercontent.com/gem/oq-engine/master/requirements-py38-linux64.txt openquake.engine
	```

This works for Linux and Python 3.8. You can trivially adapt the command to Python 3.9 and 3.10, and to other operating 
systems. For instance for Windows and Python 3.8, it would be::

	```
	$ pip install -r https://raw.githubusercontent.com/gem/oq-engine/master/requirements-py38-win64.txt openquake.engine
	```

and for Mac and Python 3.8, it would be::

	```
	$ pip install -r https://raw.githubusercontent.com/gem/oq-engine/master/requirements-py38-macos.txt openquake.engine
	```

*****
Cloud
*****

A set of `Docker containers <https://github.com/gem/oq-engine/blob/master/doc/installing/docker.md>`_ for installing the engine in the cloud.

************
Getting help
************

If you need help or have questions/comments/feedback for us, you can subscribe to the OpenQuake Engine users mailing list: 
https://groups.google.com/g/openquake-users