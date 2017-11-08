README = open("README.rst").read()

import os
import sys
from setuptools import setup

version = "2.0"

if sys.argv[-1] == 'publish':
    try:
        import wheel
        print("Wheel version: ", wheel.__version__)
        import twine
        print("Twine version: ", twine.__version__)
    except ImportError:
        print('Wheel or twine libraries missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist bdist_wheel --universal')
    os.system('twine upload dist/*')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

setup(
    name = 'python-wars-solo',
    version = version,
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
    classifiers = [
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python'
    ],
)
