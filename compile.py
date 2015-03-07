import subprocess
subprocess.call("python2 setup.py build_ext --inplace", shell=True)
subprocess.call("python2 setup.py build_ext --inplace", shell=True, cwd='core/')