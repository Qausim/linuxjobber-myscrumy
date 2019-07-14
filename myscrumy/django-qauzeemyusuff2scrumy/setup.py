import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
  name='django-qauzeemyusuff2scrumy',
  version='0.1',
  packages=find_packages(),
  include_package_data=True,
  license='BSD license',
  description='A simple app required in the Linux Jobber internship.',
  long_description=README,
  url='https://www.example.com',
  author='Olawumi Yusuff',
  author_email='qauzeemyusuff2@gmail.com',
  classifiers=[
    'Environment :: Web Environment',
    'Framework :: Django',
    'Framework :: Django :: 2.2.3',
    'Intended Audience :: Developers',
    'Licence :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
  ],
)