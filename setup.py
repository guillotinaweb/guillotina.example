import os

from setuptools import setup, find_packages

with open('README.md') as readme:
    long_desc = readme.read()

setup(name='pserver_example',
      version='0.0.1',
      description='pserver example application',
      long_description=long_desc,
      classifiers=[
          'Programming Language :: Python :: 3.5',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      packages=find_packages(),
      include_package_data=True,
      namespace_packages=[
          'pserver'
      ],
      install_requires=[
          'plone.server',
      ],
      entry_points={
          'plone.server': [
              'include = pserver.example',
          ],
      })
