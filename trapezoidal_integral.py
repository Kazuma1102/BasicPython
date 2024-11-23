#制御構文
from math import sin,pi

h=(pi/2/100)
S=0
for k in range(1,101):
         t=(h/2)*(sin((k-1)*h)+sin(k*h))
         S+=t

print(S)

