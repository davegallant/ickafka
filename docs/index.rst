.. ickafka documentation master file, created by
   sphinx-quickstart on Wed Oct 24 09:05:44 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ickafka - a kafka consumer with color
===================================

.. image:: https://badge.fury.io/py/ickafka.svg
    :target: https://badge.fury.io/py/ickafka

.. image:: https://travis-ci.org/davegallant/ickafka.svg?branch=master
    :target: https://travis-ci.org/davegallant/ickafka

.. figure:: https://user-images.githubusercontent.com/4519234/47335349-d55e6700-d658-11e8-9552-260c56caa696.gif
   :alt: ickafka_demo

Installation
------------

.. code:: bash

   pip install ickafka

Usage
*****

Start consuming at the latest offset:

.. code:: bash

   ickafka -s localhost:9092 -t my_test_topic


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   guide/advanced


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
