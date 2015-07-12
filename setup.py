import os
import re
import sys
from setuptools import setup, find_packages


PY_VER = sys.version_info

if PY_VER < (3, 4):
    raise RuntimeError("orm doesn't suppport Python earlier than 3.4")


def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()


def read_version():
    regexp = re.compile(r"^__version__\W*=\W*'([\d.abrc]+)'")
    init_py = os.path.join(os.path.dirname(__file__), 'orm', '__init__.py')
    with open(init_py) as f:
        for line in f:
            match = regexp.match(line)
            if match is not None:
                return match.group(1)
        else:
            raise RuntimeError('Cannot find version in orm/__init__.py')

classifiers = [
    'License :: OSI Approved :: BSD License',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Operating System :: POSIX',
    'Operating System :: MacOS :: MacOS X',
    'Environment :: Web Environment',
    'Development Status :: 4 - Beta',
    'Topic :: Database',
    'Topic :: Database :: Front-Ends',
]


setup(name='orm',
      version=read_version(),
      description=('ORM for asyncio-compatible SQL drivers.'),
      long_description='\n\n'.join((read('README.rst'), read('CHANGES.txt'))),
      classifiers=classifiers,
      platforms=['POSIX'],
      author='Andrew Svetlov',
      author_email='andrew.svetlov@gmail.com',
      url='http://orm.readthedocs.org',
      download_url='https://pypi.python.org/pypi/orm',
      license='Apache 2',
      packages=find_packages(),
      include_package_data=True)
