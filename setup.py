from distutils.core import setup

setup(
    name='capn',
    version='1.0.1',
    packages=['capn',],
    scripts=['bin/capn', 'bin/__capn'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.markdown').read(),
)
