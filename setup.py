from distutils.core import setup

setup(
    name='capn',
    version='1.0.2',
    packages=['capn',],
    scripts=['bin/capn', 'bin/__capn'],
    data_files=['README.markdown',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.markdown').read(),
)
