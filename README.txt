Spa is a python package for analyzing data from the coherent scattering beamline
12.0.2 at the Advanced Light Source.  The module requires numpy, scipy modules.

Features of the library:
    * Analyze X-ray photon correlation spectroscopy datasets
    * Fit 1d (x,y), 2d and 3d (image) datasets to many functions (decayed
        exponentials, Lorentzians, Gaussians)
    * Phase retrieval and data conditioning with GPU support
    * Unwrapping and wrapping centrosymmetric data
    * Rotational symmetry analysis
    * Q-dependent (rotational) and spatial memory analysis
    * Registering and merging of data for imaging
    * Simulations of single-photon XPCS data, domain generation, and random walks
    * Endstation-specific items such as Q-calculations and conversion from
        detected events to photons


To install the library make sure that the dependcies (numpy, scipy, pyfits) are installed.  Unzip the file and in the directory run:
    
    python setup.py install

