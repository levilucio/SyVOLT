Description:
    Takes a number of Himesis files, which have been compiled from rules built in Atom3, and produces the necessary artefacts for the property prover.

Files:

    PyRamify.py
    ramify_actions.py

Directories needed:
    dot/ - For output graphs
    patterns/ - For generated output Himesis files
    
    core/ and util/ - Needed for Himesis class
    
Usage:
    - Import the PyRamify class from PyRamify.py
    - 'pyramify = PyRamify()'
    - '[self.rules, self.backwardPatterns, self.backwardPatterns2Rules, self.backwardPatternsComplete, self.matchRulePatterns] = pyramify.ramify_directory("GM2AUTOSAR_MM/transformation/HimesisWOFaulty/")' where the directory contains the Himesis files to be Ramified
        - Note: Make sure that there is only one version of each rule in this directory. No faulty versions.
    - (Optional) 'self.rulesIncludingBackLinks = pyramify.getRulesIncludingBackLinks(transformation, self.backwardPatterns)' to automatically detect rules with backward links
    - Then the usual call to SymbolicStateSpace can be done    
