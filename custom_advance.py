# Output an adjacency matrix for current selection to clipborad in a "Mathematica" list fomart 
# Use AdjacencyGraph[] in Mathematica for downstream processing.
# Author: Feng Geng(shouldsee.gem@gmail.com), May 2016.

import golly as g
from glife import *
import numpy as np
import hashlib

stepmax=int(g.getstring('steps to advance','1000'))
sel=g.getselrect()
step=1
script=g.getstring('script to apply','clock2.py') #change here to your desired script
update_interval=2
xs=0.25
ys=1
while step<=stepmax:
	execfile(script)	
	g.advance(0,1)
	step=step+1
	g.setgen(str(step))
	if step%update_interval:
		g.update()
