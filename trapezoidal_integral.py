#制御構文
from math import sin,pi
a = 0
b = pi / 2
n = 100
h=(b/n)
for k in range(1,101):
         t=(h/2)*(sin((k-1)*h)+sin(k*h))
         a+=t

print(a)


