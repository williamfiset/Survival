

"""
Usage:
    python setup.py py2app
"""

__author__ = 'William Fiset'

from setuptools import setup

APP = ['main.py']
DATA_FILES = [('', ['images']), ('', ['audio'])]
OPTIONS = {'iconfile':'icon.icns',} 

setup(

    app = APP,
    data_files = DATA_FILES,
    options = {'py2app': OPTIONS},
    setup_requires = ['py2app'],

)
