from setuptools import setup

setup(
    name='worldbuild',
    version='0.1.0',
    author='Duncan Murray',
    author_email='djmurray@acutesoftware.com.au',
    packages=['worldbuild', 'worldbuild.data'],
    url='https://github.com/acutesoftware/worldbuild',
    install_requires=[
          'nose >= 1.0',
          'noise >= 1.2.1',
          'pathfinding >= 0.0.4',
          'aikif >= 0.1.4'
    ],
    include_package_data = True,
    package_data = {
        'worldbuild': ['data/*.*'],
        'worldbuild': ['samples/*.*'],
    },
    license='GNU General Public License v3 (GPLv3)',
    description='Tools for computational world building',
    long_description=open('README.txt').read(),
    classifiers = [
    'Development Status :: 4 - Beta',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    ],

)
