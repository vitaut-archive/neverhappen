neverhappen.py
==============

.. image:: it-happens.jpg

Some things should never happen. But what if they do happen?
``neverhappen.py`` got you covered. It is carefully designed to do something useless in case of events
that should never happen actually happening, so that you don't have to do it yourself.

Usage
-----

.. code-block:: python

  from neverhappen import neverhappen

  # Call this whenever you think something should never happen.
  neverhappen()

Features
--------

* Never happens
* ``neverhappen.py`` can be run from command-line with things that never happen not happening
* 100% test coverage including the part that never happens

Limitations
-----------

* The code may not cover cases that should never ever happen.
