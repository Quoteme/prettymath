#!/usr/bin/env python3
from distutils.core import setup
setup(name='prettymath',
      version='1.0',
      author='Luca Leon Happel',
      url='https://github.com/Quoteme/prettymath/',
      packages=['prettymath'],
      entry_points={"console_scripts": ["prettymath=prettymath.__main__:main"]},
      include_package_data=True,
      zip_safe=False
      )
