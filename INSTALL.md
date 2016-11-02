The Python scripts for SyVOLT will run under Python 2.7+ or Python 3.3+. Note that main development happens under Python 3.5, so this is the preferred version. Notable speed increases are also seen under Python 3.5.

SyVOLT requires a number of libraries for the Python scripts to run correctly
* igraph
* numpy
* graphviz (optional)
* pydot (optional)
* psutil (optional)

These libraries are best installed through your package manager. However, difficulties can arise with igraph, so further instructions are below.


# Linux


## IGRAPH:

SyVOLT requires the Python bindings to the igraph C library.

The difficulty is in making sure that the bindings are for the correct version of Python, either 2 or 3.

The easiest way of obtaining these bindings is by using your package manager (below example is for Ubuntu):

`sudo apt-get install python-igraph`

or

`sudo apt-get install python3-igraph`


If that doesn't work, try other package managers:

###PIP:

`sudo apt-get install python-pip`

`sudo pip install python-igraph`

or

`sudo apt-get install python3-pip`

`sudo pip install python-igraph`


# Mac

Install Homebrew first (http://brew.sh/)

Then install PIP (comes with python):

`brew install python3`

## IGRAPH:

`sudo pip3.5 install python-igraph`

## numpy:

`sudo pip3 install numpy`


# From Source

If the previous work, you'll have to install from source

* Try installing the igraph C part from your package manager first

`sudo apt-get install libigraph0v5`

`sudo apt-get install libigraph0-dev`

* Download the python-igraph source code at http://igraph.org/python/ under the Downloads section.
* Unzip the archive
* `python setup.py install`
* or `python3 setup.py install`



