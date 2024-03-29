from __future__ import print_function
from distutils.core import setup, Extension
from distutils.sysconfig import get_python_inc, get_python_lib
import os
import sys
import numpy

###################################################################

define_macros = []
undef_macros = []
extra_compile_args = []
include_dirs = []

ppgplot_libraries = ["cpgplot", "pgplot", "X11", "png", "m", "gfortran"]
ppgplot_library_dirs = ["/usr/X11R6/lib"]

make_extension = Extension
include_dirs.append(numpy.get_include())
ppgplot_include_dirs = include_dirs
presto_include_dirs = include_dirs
undef_macros.append('USE_NUMARRAY')

if os.name == "posix":
    if "PGPLOT_DIR" in os.environ:
        ppgplot_library_dirs.append(os.environ["PGPLOT_DIR"])
        ppgplot_include_dirs.append(os.environ["PGPLOT_DIR"])
    else:
        print("PGPLOT_DIR env var not defined!", file=sys.stderr)
else:
    raise Exception("os not supported")

ext_ppgplot = make_extension('_ppgplot',
                             [os.path.join('src','_ppgplot.c')],
                             include_dirs=ppgplot_include_dirs,
                             libraries=ppgplot_libraries,
                             library_dirs=ppgplot_library_dirs,
                             define_macros=define_macros,
                             extra_compile_args=extra_compile_args)

###################################################################

setup(name="ppgplot",
      version="1.0",
      description="Python (2/3) interfaces to PGPLOT",
      author="Nick Patavlis/Scott Ransom/Matteo Bachetti/Cees Bassa",
      author_email="",
      packages=['ppgplot'],
      package_dir={'ppgplot':'src'},
      ext_modules=[ext_ppgplot])
