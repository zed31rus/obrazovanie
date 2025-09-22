from math import *

x = 12.3*(10**-1)
y=15.4
z=0.252*(10**3)

ch1 = y**(x+1)
ch2 = x + y/2
z1 = ((abs(y-2))**(1/3))+ 3
z2 = 2*abs(x+y)
o1 = (x+1)**(-1/sin(z))

d1 = ch1/z1
d2 = ch2/z2

s = d1+(d2*o1)
print(s)