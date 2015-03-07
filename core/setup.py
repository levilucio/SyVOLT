from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

extensions = [
    Extension("himesis", ["./*.pyx"],
        include_dirs = ["/usr/include/igraph/"],
        libraries = ["igraph"],
        library_dirs = ["/usr/lib/"]
    )
]

setup(
  name = 'himesis',
  ext_modules = cythonize(extensions,
  compiler_directives={'profile': False}
  ),
)
