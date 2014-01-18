notify
==========================
.. image:: https://secure.travis-ci.org/lambdalisue/notify.png?branch=master
    :target: http://travis-ci.org/lambdalisue/notify
    :alt: Build status

.. image:: https://coveralls.io/repos/lambdalisue/notify/badge.png?branch=master
    :target: https://coveralls.io/r/lambdalisue/notify/
    :alt: Coverage

.. image:: https://pypip.in/d/notify/badge.png
    :target: https://pypi.python.org/pypi/notify/
    :alt: Downloads

.. image:: https://pypip.in/v/notify/badge.png
    :target: https://pypi.python.org/pypi/notify/
    :alt: Latest version

.. image:: https://pypip.in/wheel/notify/badge.png
    :target: https://pypi.python.org/pypi/notify/
    :alt: Wheel Status

.. image:: https://pypip.in/egg/notify/badge.png
    :target: https://pypi.python.org/pypi/notify/
    :alt: Egg Status

.. image:: https://pypip.in/license/notify/badge.png
    :target: https://pypi.python.org/pypi/notify/
    :alt: License

Notify process termination via email

Installation
------------
Use pip_ like::

    $ pip install notify

.. _pip:  https://pypi.python.org/pypi/pip

Usage
--------
1.  Running *notify* with following command will start setup wizard first time.
    ::

        $ notify

2.  Follow the setup wizard instruction

3.  Check with the following command (Only for Unix system)
    ::

        $ notify --check

4.  Use *notify* like
    ::

        $ notify really_havy_process -a -b --options
        $ notify -t different@address.com really_havy_process -a -b --options
