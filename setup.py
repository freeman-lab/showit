#!/usr/bin/env python

import json
from setuptools import setup

with open('VERSION', 'r') as fh:
    version = json.loads(fh.read())

setup(
    name='showit',
    version=version['string'],
    description='simple and sensible display of images',
    author='freeman-lab',
    author_email='the.freeman.lab@gmail.com',
    packages=['showit'],
    url='https://github.com/freeman-lab/showit',
    install_requires=open('requirements.txt').read().split(),
    long_description='See https://github.com/freeman-lab/showit',
    data_files=[('share/showit', ['VERSION'])],
)
