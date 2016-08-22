=======
IGRAPH:

SyVOLT requires the Python bindings to the igraph C library.

The difficulty is in making sure that the bindings are for the correct version of Python, either 2 or 3.

The easiest way of obtaining these bindings is by using your package manager (below example is for Ubuntu):

sudo apt-get install python-igraph
or
sudo apt-get install python3-igraph


If that doesn't work, try other package managers:

PIP:

sudo apt-get install python-pip
sudo pip install python-igraph
or
sudo apt-get install python3-pip
sudo pip install python-igraph


If that doesn't work, you'll have to install from source

- Try installing the igraph C part from your package manager first
sudo apt-get install libigraph0v5
sudo apt-get install libigraph0-dev

- Download the python-igraph source code at http://igraph.org/python/ under the Downloads section.
- Unzip the archive
- python setup.py install
- or python3 setup.py install


