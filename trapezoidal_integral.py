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

#関数
import math

def trapezoidal_integration(f, a=0, b=1, n=100):
   
    h = (b - a) / n  
    result = 0.5 * (f(a) + f(b))  
    for i in range(1, n):
        result += f(a + i * h) 
    return result * h

# (1) 
def f1(x):
    return math.sin(x)
result1 = trapezoidal_integration(f1, 0, math.pi / 2, 50)
print(f"(1) 結果: {result1}")

# (2) 
def f2(x):
    return 4 / (1 + x**2)
result2 = trapezoidal_integration(f2, 0, 1, 100)
print(f"(2) 結果: {result2}")

# (3) 
def f3(x):
    return math.sqrt(math.pi) * math.exp(-x**2)
result3 = trapezoidal_integration(f3, -100, 100, 1000)
print(f"(3) 結果: {result3}")



