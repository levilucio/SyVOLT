try:
    import igraph
except ImportError:
    import sys
    error_string = "Required Python bindings for igraph not found!\n"
    error_string += "Please follow the instructions in INSTALL.txt file to install bindings.\n"
    error_string += "Current version of Python: " + str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "\n"
    error_string += "sys.path:\n"
    for p in sys.path:
        error_string += str(p) + "\n"
    raise Exception(error_string)