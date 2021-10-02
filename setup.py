from os import path
from setuptools import setup

version = "0.3.4"

directory = path.abspath(path.dirname(__file__))
with open(path.join(directory, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='hypercomplex',
    version=version,
    author='discretegames',
    author_email='discretizedgames@gmail.com',
    description="Library for arbitrary-dimension hypercomplex numbers following the Cayley-Dickson construction.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/discretegames/hypercomplex',
    project_urls={"GitHub": "https://github.com/discretegames/hypercomplex",
                  "PyPI": "https://pypi.org/project/hypercomplex",
                  "TestPyPI": "https://test.pypi.org/project/hypercomplex"},
    packages=['hypercomplex'],
    python_requires='>=3.6',
    install_requires=['mathdunders>=0.4.1'],
    license="MIT",
    keywords=['python', 'math', 'complex', 'number', 'hypercomplex', 'Cayley', 'Dickson', 'construction',
              'algebra', 'quaternion', 'octonion', 'sedenion', 'pathion', 'chingon', 'routon', 'voudon'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ]
)
