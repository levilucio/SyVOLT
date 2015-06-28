import subprocess
import sys
import os

from core.himesis_utils import load_class


graph_dirs = ["property_prover_rules/cardinality_resolution/Himesis/",
             "property_prover_rules/disambiguation_rules/Himesis/",
             "property_prover_rules/traceability_resolution/Himesis/"]


for graph_dir in graph_dirs:
    try:
        files = os.listdir(graph_dir)
    except OSError:
        print("Warning: " + graph_dir + " does not exist")
        files = []

    for f in files:
        if f == "__init__.py" or not f.endswith(".py") or f.startswith("."):
            continue

        print("Examining " + graph_dir + f)

        graph_file = graph_dir + f


        #subprocess.call("python2 reindent.py " + graph_file, shell=True)

        try:
            g = load_class(graph_file)
        except ImportError:
            print("ERROR " + graph_file)
            continue

        name = g.keys()[0]
        graph = g.values()[0]

        # need to compile rule back in order to update the file
        graph.compile(graph_dir)