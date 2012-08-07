# -*- encoding: utf-8 -*-

from setuptools import setup
from mapgen.version import VERSION

config = {
    'description': 'Trying out map generator ideas.',
    'author': 'Janno Põldma',
    'url': 'https://github.com/janno-p/mapgen.git',
    'download_url': '',
    'author_email': 'janno.poldma@gmail.com',
    'version': VERSION,
    'install_requires': ['nose', 'pyglet'],
    'packages': ['mapgen'],
    'scripts': ['bin/mapgen', 'bin/mapgen.bat'],
    'name': 'mapgen',
}

setup(**config)
