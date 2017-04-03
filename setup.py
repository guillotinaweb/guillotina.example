import os

from setuptools import setup

with open('README.md') as readme:
    long_desc = readme.read()

setup(name='example',
      version='1.0.0',
      description='guillotina example application',
      long_description=long_desc,
      classifiers=[
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      packages=[
          'example',
      ],
      include_package_data=True,
      install_requires=[
          'guillotina',
      ],
      entry_points={
          'guillotina': [
              'include = example',
          ],
      })
