try:
    from setuptools import setup:
except ImportError:
    from distutils.core import setup

config = {
 'description': 'multiprocessing web scraper  for  e commerce website scraping ',
 'author': 'Maytham Alherz',
 'url': '',
 'download_url': '',
 'author_email': 'gmaytham@gmail.com',
 'version': '0.1',
 'install_requires': [''],
 'packages': [''],
 'scripts': [],
 'name': 'scraper'
}

 setup(**config)
