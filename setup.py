#!/usr/bin/env python3
from setuptools import setup
setup(name='prettymath',
      version='1.0',
      author='Luca Leon Happel',
      url='https://github.com/Quoteme/prettymath/',
      py_modules=['prettymath'],
      entry_points = {"console_scripts": ['prettymath = prettymath:main']},
      include_package_data=True,
      zip_safe=False
      )
