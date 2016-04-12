
.. _environment-setup:

Development Environment Setup
=============================

.. _setup-python:

Setup Python
------------

`Download and install the latest Python 2.7.X <https://www.python.org/downloads/>`_

Open the command line and run the following commands::

   pip install flake8
   pip install pep8
   pip install pyflakes


.. _download-atom:

Downloading Atom
----------------

The recommended text editor for modding Crea is Atom. Atom supports syntax highlighting and many packages to make your life easier.

`Download Atom Here <http://atom.io/>`_

.. _install-atom:

Setting Up Atom
---------------

Once Atom has been installed you will want to setup the packages.

 * `File Types Package <https://atom.io/packages/file-types>`_
 * `Linter Package <https://atom.io/packages/linter>`_
 * `Flake8 Linter Package <https://atom.io/packages/linter-flake8>`_
 * `Pep8 Linter Package <https://atom.io/packages/linter-pep8>`_
 * `Pyflakes Linter Package <https://atom.io/packages/linter-pyflakes>`_

Setup both linter-pep8 and linter-flake8 to ignore error code 'E251' and have a max line length of 300.

'Open Your Config' and add to the bottom the following::

   "file-types":
     ce: "source.python"
