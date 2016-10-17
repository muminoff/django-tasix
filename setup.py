#!/usr/bin/env python

from setuptools import setup
import re
import os
import sys


def get_packages(package):
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


setup(
    name='django-tasix',
    version='0.1.0',
    url='https://github.com/muminoff/django-tasix',
    license='MIT',
    description='Simple django app to allow/block IP addresses and ranges outside the Tas-IX network',
    long_description=open('Readme.md', 'r').read(),
    author='Sardor Muminov',
    author_email='smuminov@gmail.com',
    packages=get_packages('tasix'),
    package_data=get_package_data('.'),
    install_requires=[
        'netaddr',
    ],
    tests_require=['django'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
