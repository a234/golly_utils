# Output an adjacency matrix for current selection to clipborad in a "Mathematica" list fomart 
# Use AdjacencyGraph[] in Mathematica for downstream processing.
# Author: Feng Geng(shouldsee.gem@gmail.com), May 2016.

import golly as g
from glife import *
import numpy as np
import hashlib

rule=g.getrule()
ruleB=rule.split('/')[0][1:]
ruleS=rule.split('/')[1][1:]
S=['S']
B=['B']
for i in range(9):
	if not str(i) in ruleB:
		S.append(str(8-int(i)))
	if not str(i) in ruleS:
		B.append(str(8-int(i)))

B=''.join(B)
S=''.join(S)
gen=int(g.getgen())
rules=['','']
invrule='/'.join([B,S])
if str(0) not in ruleB:
	tp=rule
	rule=invrule
	invrule=tp

rules[gen%2]=rule;
rules[(gen+1)%2]=invrule;

# g.note(rule)

#g.setrule(invrule)
speed=2
rules=[rule,invrule]
while True:
	gen=int(g.getgen())	
	g.setrule(rules[gen%2])
	g.run(1)
	if gen%speed==0:
		g.update()	

	
