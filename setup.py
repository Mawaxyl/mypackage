from setuptools import setup, find_packages

setup(
    name = 'mypackage',
    version = '0.1',
    package = find_packages(exclude=['tests*']),
    license = 'MIT',
    description = 'EDSA example python package',
    long_description = open('README.md').read(),
    install_requires = ['numpy'],
    url = "https://github.com/<Mawaxyl>/<mypackage>",
    author = 'Mukthar',
    author_email = 'mukhyolakunle@gmail.com'
)