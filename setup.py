# coding=utf-8
import sys
from setuptools import setup, find_packages

NAME = 'notify'
VERSION = '0.1.11'

def read(filename):
    import os
    BASE_DIR = os.path.dirname(__file__)
    filename = os.path.join(BASE_DIR, filename)
    fi = open(filename, 'r')
    return fi.read()

def readlist(filename):
    rows = read(filename).split("\n")
    rows = [x.strip() for x in rows if x.strip()]
    return list(rows)

extras = {}
if sys.version_info >= (3,):
    extras['use_2to3'] = True

setup(
    name = NAME,
    version = VERSION,
    description = 'Notify process termination via email',
    long_description = read('README.rst'),
    classifiers = (
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ),
    keywords = 'mail note notification notify cui command',
    author = 'Alisue',
    author_email = 'lambdalisue@hashnote.net',
    url = 'https://github.com/lambdalisue/%s' % NAME,
    download_url = 'https://github.com/lambdalisue/%s/tarball/master' % NAME,
    license = 'MIT',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data = True,
    package_data = {
        '': ['LICENSE', 'README.rst',
             'requirements.txt',
             'requirements-test.txt',
             'requirements-docs.txt'],
    },
    zip_safe=True,
    install_requires=readlist('requirements.txt'),
    entry_points={
        'console_scripts': [
            'notify = notify.console:main',
        ],
    },
    **extras
)
