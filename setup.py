from setuptools import setup

setup(
    name='worldbuild',
    version='0.0.1',
    author='Duncan Murray',
    author_email='djmurray@acutesoftware.com.au',
    packages=['worldbuild', 'worldbuild.data'],
    url='https://github.com/acutesoftware/worldbuild',
    install_requires=[
          'nose >= 1.0',
          'noise >= 1.2.1',
          'aikif >= 0.1.3'
    ],
    include_package_data = True,
    package_data = {
        'worldbuild': ['data/*.*'],
    },   
    license='LICENSE.txt',
    description='Tools for computational world building',
    long_description=open('README.rst').read(),
    classifiers = [
    'Development Status :: 1 - Planning',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Games/Entertainment :: Simulation',
    'Topic :: Scientific/Engineering :: Artificial Life',
    ],

)