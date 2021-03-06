# Output an adjacency matrix for current selection to clipborad in a "Mathematica" list fomart 
# Use AdjacencyGraph[] in Mathematica for downstream processing.
# Author: Feng Geng(shouldsee.gem@gmail.com), May 2016.

import golly as g
from glife import *
import numpy as np
import hashlib

pt=g.getcells(g.getrect());
width=g.getstring('width of torus','200')
rule=g.getrule()
nrule=rule.split(':')[0]+':T{},512'.format(width);
g.note(nrule);
g.setrule(nrule);

