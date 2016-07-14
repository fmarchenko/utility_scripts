import os
import sys
from setuptools import setup

install_requires = []
binpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bin')

if os.name == 'posix':
    install_requires.append('termcolor>=1.1.0')

version = sys.version_info[:2]

if version < (2,7) or (3,0) <= version <= (3,1):
    install_requires += ['argparse']

setup(
    name='utility-scripts',
    version='0.1.0',
    description='Tool for working with Linux OS.',
    long_description=open('README.md').read(),
    license='MIT License',
    author='Fedor Marchenko',
    author_email='mfs90@mail.ru',
    url='https://github.com/fmarchenko/utility_scripts',
    zip_safe=False,
    packages=['utility_scripts', 'utility_scripts.lib'],
    scripts=map(lambda x: os.path.join(binpath, x), os.listdir(binpath)),
    platforms='any',
    install_requires=install_requires,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Database',
        'Topic :: Utilities'
        ],
    keywords='',
    )
