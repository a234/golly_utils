# A randomized rectangle filler for use with Golly.
# Author: Nathaniel Johnston (nathaniel@nathanieljohnston.com), June 2009.
#
# Even though Golly comes built-in with the golly.randfill() function, there
# does not seem to be a way to seed that function, so you get the same sequence
# of random rectangles every time you reload Golly. This script eliminates that
# problem.


import golly as g
import random
random.seed()

pop=int(g.getpop())
rect=g.getrect()
g.select(rect)
g.clear(0)
i=1;
while i<=pop:
	x=random.randint(rect[0],rect[0]+rect[2]-1)
	y=random.randint(rect[1],rect[1]+rect[3]-1)
	if g.getcell(x,y)!=1:
		g.setcell(x,y,1)
		i=i+1;
	else:
		continue	
#g.note(str(i))


