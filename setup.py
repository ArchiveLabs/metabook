#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    setup.py
    ~~~~~~~~

    Metabook - one metadata entry for every book

    :copyright: (c) 2016 by mek.
    :license: see LICENSE for more details.
"""

import codecs
import os
import re
from setuptools import setup
from metabook import __desc__

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """Taken from pypa pip setup.py:
    intentionally *not* adding an encoding option to open, See:
       https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    """
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

def requirements():
    with open('requirements.txt') as dependencies:
        return dependencies.read()

setup(
    name='metabook',
    version=find_version("metabook", "__init__.py"),
    description=__desc__,
    long_description=read('README.md'),
    classifiers=[
        ],
    author='Archive Labs',
    author_email='mek@archive.org',
    url='https://github.com/ArchiveLabs/metabook',
    packages=[
        'metabook'
        ],
    platforms='any',
    license='LICENSE',
    install_requires=requirements()
)
