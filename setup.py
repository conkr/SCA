try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='spa',
    version='0.1',
    #requires = ['scipy', 'numpy'],
   # package_data = { 'speckle': ['gpu/kernels/*.cl']},
    author = "Run Su",
    author_email = "runnever@gmail.com",
    packages=['spa'],
    install_requires=[ 'numpy','scipy' ],
    description = "python package for scattering and imaging data analysis at Beamline 12.0.2 at the Advanced Light Source",
    url = "https://sites.google.com/a/lbl.gov/coherent-scattering-beamline/"
)
  
