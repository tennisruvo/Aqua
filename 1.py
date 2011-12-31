# -*- coding: utf-8 -*-
from string import split
a,b=map(int, split(raw_input()))
c=max(a,b)
d=min(a,b)
for x in reversed(range(1, min(a,b)+1)):
        if c%x==0 and d%x==0:
        	break

f=(a*b)/x
if (a*b)<0:
        f=(-1*(a*b))/x
print x, f
		
