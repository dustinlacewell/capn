from setuptools import setup

setup(
    name='capn',
    version='1.0rc1',
    packages=['capn',],
    scripts=['bin/capn', 'bin/__capn'],
    install_requires=['PyYAML'],
    provides=['capn'],
    author="Dustin Lacewell",
    author_email="dlacewell@gmail.com",
    url="https://github.com/dustinlacewell/capn",
    description="capn provides hooks on working-directory change.",
    long_description=open("README.markdown", 'r').read(),
)
