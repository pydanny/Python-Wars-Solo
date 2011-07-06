README = open("README.rst")

import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'Python Wars Solo',
    version = '1.0.0',
    description = "A retro-style Apple ][ Basic game cooked up in 45 minutes",
    license = 'GPL',
    long_description = README,
    url = 'https://github.com/pydanny/Python-Wars-Solo',
    
    author = 'Daniel Greenfeld',
    author_email = 'pydanny@gmail.com',
    
    py_modules =  ['go.py','stuff.py'],
    
    classifiers = (
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
    ),
)
