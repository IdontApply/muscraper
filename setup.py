from setuptools import find_packages, setup

with open('README.txt') as f:
 long_description = f.read()

setup(
 description='multiprocessing web scraper  for  e commerce website scraping',
 url='https://github.com/IdontApply/muscraper',
 long_description=long_description,
 author='Maytham Alherz',
 author_email='gmaytham@gmail.com',
 version='0.0.1',
 packages=['sescrp'],
 name='muscraper',
 license='Apache 2.0',
 install_requires=[],
)


