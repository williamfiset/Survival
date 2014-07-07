

"""
Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = [('', ['images']), ('', ['audio'])]
OPTIONS = {'iconfile':'icon.icns',} # 'argv_emulation': False/True 

setup(

    app = APP,
    data_files = DATA_FILES,
    options = {'py2app': OPTIONS},
    setup_requires = ['py2app'],

)