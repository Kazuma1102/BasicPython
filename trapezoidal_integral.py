

#関数
import math

def trapezoidal_integration(f, a=0, b=1, n=100):

    h = (b - a) / n  
    result = 0.5 * (f(a) + f(b))  
    for i in range(1, n):
        result += f(a + i * h) 
    return result * h

 #1番

def fa(x):
    return math.sin(x)
result1 = trapezoidal_integration(fa, 0, math.pi / 2, 50)
print(f"(1) 解答: {result1}")

#2番

def f2(x):
    return 4 / (1 + x**2)
result2 = trapezoidal_integration(f2, 0, 1, 100)
print(f"(2) 解答: {result2}")

#3番

def f3(x):
    return math.sqrt(math.pi) * math.exp(-x**2)

result3 = trapezoidal_integration(f3, -100, 100, 1000)
print(f"(3) 解答: {result3}")

print("変更テストこの文章は無視してください,")