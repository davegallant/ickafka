.. _advanced:

Advanced Usage
==============

To specify a consumer group name (default is None):

.. code:: bash

   ickafka -s localhost:9092 -t my_test_topic -g testgroup

Consume all messages from the earliest offset:

.. code:: bash

   ickafka -s localhost:9092 -t my_test_topic -o earliest

Capture all consumed messages into a json file:

.. code:: bash

   ickafka -s localhost:9092 -t my_test_topic --capture

Disabling color:

.. code:: bash

   ickafka -s localhost:9092 -t my_test_topic --no-color
