#!/usr/bin/env python
# coding=utf8

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='pypi-classifiers',
      version='0.2',
      description=('Use a GUI to select PyPI-classifiers and include them in a'
                   'setup.py'),
      long_description=read('README.rst'),
      keywords='pypi setup.py classifiers programming',
      author='Marc Brinkmann',
      author_email='git@marcbrinkmann.de',
      url='http://github.com/mbr/pypi-classifiers',
      license='MIT',
      scripts=[
          'pypi-classifiers',
      ],
      install_requires=['requests'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Win32 (MS Windows)',
          'Environment :: X11 Applications :: GTK',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development',
          'Topic :: Utilities',
      ], )
