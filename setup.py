import os
import re

from setuptools import find_packages
from setuptools import setup


def get_long_description():
    with open('README.rst', 'r') as f:
        return f.read()


def get_version(package):
    with open(os.path.join(package, '__init__.py')) as f:
        pattern = r'^__version__ = [\'"]([^\'"]*)[\'"]'
        return re.search(pattern, f.read(), re.MULTILINE).group(1)


setup(
    name='arcgis-sdk',
    version=get_version('arcgis_sdk'),
    license='MIT',
    description='Python SDK for Arcgis API',
    long_description=get_long_description(),
    author='mongkok',
    author_email='dani.pyc@gmail.com',
    maintainer='mongkok',
    url='https://github.com/mongkok/arcgis-sdk/',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'requests>=2.14.2'
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    zip_safe=False,
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest>=3.0.7',
        'requests>=2.14.2',
        'responses>=0.5.1'
    ]
)
