# 関数
#ユークリッドの互除法

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

result = gcd(48, 18)
print(result)  


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def are_coprime(a, b):
    return gcd(a, b) == 1

#互いに素
a = 15
b = 28

if are_coprime(a, b):
    print(f"{a} と {b} は互いに素です。")
else:
    print(f"{a} と {b} は互いに素ではありません。")
