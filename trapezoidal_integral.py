#制御構文
from math import sin

π=3.14159265359
h=(π/2/100)
S=0
for k in range(100):
                   t=(h/2)*(sin((k-1)*h)+sin(k*h))
                   S+=t

print(S)

#関数
a=0
b=1
n=100
π=3.14159265359
h=(π/2/n)

from math import sin, exp, pi, sqrt


def trapezoidal(f, a, b, n):
    h = (b - a) / n 
    integral = 0.5 * (f(a) + f(b))  
    for i in range(1, n):
        integral += f(a + i * h)
    return integral * h
        
    
        
        
def f1(x):
        return sin(x)
result1 = trapezoidal(f1, 0, pi / 2, 50)
print(f"(1) sin(x) の積分結果: {result1}")

def f2(x):
        return 4/(1+x**2)
result2 =trapezoidal(f2,0,1,100)
print(f"4/(1+x**2)の積分結果:{result2} ")

def f3(x):
        return sqrt(pi) * exp(-x**2)
result3=trapezoidal(f3,-100,100,1000)
print({f" √(π)exp⁡(−x^2)の積分結果:{result3}"})
