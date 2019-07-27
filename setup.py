try:
    from setuptools import setup:
except ImportError:
    from distutils.core import setup

config = {
 'description': 'First go on making a web web scarper',
 'author': 'Maytham Alherz',
 'url': 'URL to get it at.',
 'download_url': 'Where to download it.',
 'author_email': 'My email.',
 'version': '0.1',
 'install_requires': ['nose'],
 'packages': ['scrp'],
 'scripts': [],
 'name': 'scraper'
}

 setup(**config)
