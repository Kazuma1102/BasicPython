#制御構文
<<<<<<< HEAD
from math import sin,pi

h=(pi/2/100)
S=0
for k in range(1,101):
         t=(h/2)*(sin((k-1)*h)+sin(k*h))
         S+=t

print(S)

=======
from math import sin
from math import pi

h=(pi/2/100)
S=0
for k in range(100):
    t=(h/2)*(sin((k-1)*h)+sin(k*h))
    S+=t

print(S)


>>>>>>> f8631dfb736b9475037882e09acab4677b88dab5
