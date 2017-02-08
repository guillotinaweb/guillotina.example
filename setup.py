import os

from setuptools import setup, find_packages

requires = [
    'plone.server',
    ]

setup(name='pserver_example',
      version='0.0.1',
      description='pserver example applciation',
      author='Joel Kleier',
      author_email='joel@kleier.us',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points={
          'plone.server': [
              'include = pserver.example',
          ],
      })
