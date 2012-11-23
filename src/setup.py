#! /usr/bin/env python
#
# Edward Loper's (modified) API Documentation Generation Tool
#
# Created [05/27/01 09:04 PM]
# Edward Loper
#

from distutils.core import setup
import re, sys, epycsdoc

VERSION = str(epycsdoc.__version__)
(AUTHOR, EMAIL) = re.match('^(.*?)\s*<(.*)>$', epycsdoc.__author__).groups()
URL = epycsdoc.__url__
LICENSE = epycsdoc.__license__
KEYWORDS='docstring restructuredtext rst javadoc docformat pydoc epycsdoc'
LONG_DESCRIPTION = """\
Epydoc is a tool for generating API documentation documentation for
Python modules, based on their docstrings.  For an example of epycsdoc's
output, see the API documentation for epycsdoc itself (`html
<http://epycsdoc.sf.net/api/>`__\ , `pdf
<http://epycsdoc.sf.net/epycsdoc.pdf>`__\ ).  A lightweight markup
language called `epytext <http://epycsdoc.sf.net/epytextintro.html>`__
can be used to format docstrings, and to add information about
specific fields, such as parameters and instance variables.  Epydoc
also understands docstrings written in `reStructuredText
<http://docutils.sourceforge.net/rst.html>`__\ , Javadoc, and
plaintext. For a more extensive example of epycsdoc's output, see the
API documentation for `Python 2.5
<http://epycsdoc.sourceforge.net/stdlib/>`__\ ."""
CLASSIFIERS=[
    'Development Status :: Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Topic :: Documentation',
    'Topic :: Software Development :: Documentation',
    ]

# Classifiers metadata only supported for Python 2.4+
if sys.version_info[:2] >= (2,4):
    other_metadata = dict(classifiers=CLASSIFIERS)
else:
    other_metadata = {}

if '--format=wininst' in sys.argv:
    SCRIPTS = ['scripts/epycsdoc.pyw', 'scripts/epycsdoc.py']
else:
    SCRIPTS = ['scripts/epycsdoc', 'scripts/epycsdocgui']

SCRIPTS.append('scripts/apirst2html.py')

setup(name="epycsdoc",
      description="Edward Loper's (modified) API Documentation Generation Tool",
      version=VERSION,
      author=AUTHOR,
      author_email=EMAIL,
      license=LICENSE,
      url=URL,
      scripts=SCRIPTS,
      keywords=KEYWORDS.split(),
      long_description=LONG_DESCRIPTION,
      packages=['epycsdoc', 'epycsdoc.markup', 'epycsdoc.test', 'epycsdoc.docwriter'],
      **other_metadata)

