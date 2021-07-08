from os import path
from setuptools import setup

version = "0.1.4"

directory = path.abspath(path.dirname(__file__))
with open(path.join(directory, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='hypercomplex',
    version=version,
    author='discretegames',
    author_email='discretizedgames@gmail.com',
    description="Library for arbitrary hypercomplex numbers following the Cayley-Dickson construction.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/discretegames/hypercomplex',
    packages=['hypercomplex'],
    install_requires=['mathdunders>=0.4.1'],
    license="MIT",
    keywords=['python', 'math', 'complex', 'number', 'hypercomplex', 'Cayley',
              'Dickson', 'construction', 'algebra', 'quaternion', 'octonion', 'sedenion']
)
