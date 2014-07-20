README = open("README.rst").read()

import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'python-wars-solo',
    version = '1.0.2',
    description = "A retro-style Apple ][ Basic game cooked up in 45 minutes",
    license = 'GPL',
    long_description = README,
    url = 'https://github.com/pydanny/Python-Wars-Solo',
    author = 'Daniel Greenfeld',
    author_email = 'pydanny@gmail.com',
    py_modules =  ['go','stuff', ],
    entry_points={
        'console_scripts': [
            'pythonwarsolo = go:main',
        ]
    },
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
