 

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import os
def read(fname):
     with open(fname) as f:
        return f.read()
setup(
    name='spa',
    version='0.1',
    #requires = ['scipy(>0.1, !=0.2)', 'numpy(>0.1)'],
   # package_data = { 'speckle': ['gpu/kernels/*.cl']},
    author = "conkr",
    author_email = "conkr2014@yahoo.com",
    packages=['spa'],
    install_requires=[ 'numpy','scipy' ],
    scripts=['bin/helloworld'],
    test_suite='nose.collector',
    tests_require=['nose'],
    description = "Python package for scattering and imaging data analysis",
 #   long_description=read('README.txt'),
  #  url = "https://sites.google.com/a/lbl.gov/coherent-scattering-beamline/"
)
  
