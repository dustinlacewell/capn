from distutils.core import setup

from ark import VERSION

setup(
    name='capn',
    version=VERSION,
#    packages=['capn',],
    scripts=['bin/capn', 'bin/__capn'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.markdown').read(),
)
