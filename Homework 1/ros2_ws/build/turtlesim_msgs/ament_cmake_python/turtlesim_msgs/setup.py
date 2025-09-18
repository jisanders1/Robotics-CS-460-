from setuptools import find_packages
from setuptools import setup

setup(
    name='turtlesim_msgs',
    version='1.10.1',
    packages=find_packages(
        include=('turtlesim_msgs', 'turtlesim_msgs.*')),
)
