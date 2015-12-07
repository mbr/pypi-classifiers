PyPI classifiers selector
=========================

A small GTK program that loads a list of classifiers from PyPI, displays them
in a list with checkboxes. The user can then check any number of checkboxes
and the program will generate code suitable to copy & paste into a setup.py
script.

.. image:: https://github.com/mbr/pypi-classifiers/raw/master/Screenshot.png


Installation
------------

``pypi-classifiers`` has three dependencies: GTK, Glib and `requests
<python-requests.org>`_. Most Linux desktop-oriented Linux distros ship these
as packages, which are often installed by default. Beyond this, the script is
self-contained; instead of installing into a virtualenv, it maybe possible to
just copy
`pypi-classifiers
<https://raw.githubusercontent.com/mbr/pypi-classifiers/master/pypi-classifiers>`_
somewhere and run it::

    ./pypi-classifiers

PyPI
~~~~

Installation from PyPI works as well (and will install the potentially missing
``requests`` dependency), although Gtk should be installed using your
distributions package manager (remember to ``toggleglobalsitepackages``).
