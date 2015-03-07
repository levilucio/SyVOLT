from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension


setup(
  name = 'Property Prover',
  ext_modules = cythonize([Extension("prop_prover", ["./**/*.pyx"], libraries=["igraph"])],
  ),
)