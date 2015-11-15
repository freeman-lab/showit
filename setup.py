#!/usr/bin/env python

from setuptools import setup
import showit

setup(
    name='showit',
    version=showit.__version__,
    description='simple and sensible display of images',
    author='freeman-lab',
    author_email='the.freeman.lab@gmail.com',
    packages=['showit'],
    url='https://github.com/freeman-lab/showit',
    install_requires=open('requirements.txt').read().split(),
    long_description='See https://github.com/freeman-lab/showit'
)
