Crea's Official Modding Documentation
========

This is the official repository for Crea's modding documentation. The contents include the core documentation as well as tutorials and anything else related to helping Crea modders. I plan to build onto this over time but wanted to open it up for anyone to contribute.

http://playcrea.com

Contributing
------------

You want to contribute? Great! Please follow the standard [forking](https://help.github.com/articles/fork-a-repo) and [sending pull requests](https://help.github.com/articles/using-pull-requests) procedures. The goal is to get the documentation close to something like [Python's Documentation](http://python.org/doc/). Consequently, it is highly recommended to read their [documentation guide](http://docs.python.org/devguide/documenting.html).

This documentation is built using [Sphinx](http://sphinx-doc.org/). Their site is a great source for learning how to work with Sphinx.

One thing to note is that the src/api folder is generated from the engine source and consequently should not be edited directly. If there are changes you'd like to suggest for these files then create an issue or contact me directly.

Building
--------

Run 'make html' and the output will be placed into build/.
