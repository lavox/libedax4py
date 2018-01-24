#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='libedax4py',
    version='0.1.1',
    description='Python wrapper for libedax.',
    long_description='Python wrapper for libedax.',
    author='lavox',
    author_email='lavox8@icloud.com',
    url='https://github.com/lavox/libedax4py',
    license='GPLv3',
    packages=find_packages(exclude=['data', 'example']),
    package_data={
        'libedax4py': ['libedax.dylib'],
    },
)
