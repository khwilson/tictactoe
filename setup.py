from os import path
from setuptools import setup, find_packages


def parse_requirements(file_name):
    with open(path.join(path.dirname(__file__), file_name), 'r') as f:
        return [l.strip() for l in f if not l.startswith('#')]

setup(
    name='tictactoe',
    version='0.0.1',
    url='https://github.com/khwilson/tictactoe',
    author='Benjamin Pollack',
    author_email='benjamin@bitquabit.com',
    license='BSD',
    packages=find_packages(),
    scripts=['bin/tictactoe'],
    include_package_data=True,
    zip_safe=False,
    install_requires=parse_requirements('requirements.txt'),
    description='An extremely simple python tic tac toe web game.',
    long_description=open('README.rst').read()
)
