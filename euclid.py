#制御構文
try:
    

    a = int(input("8177"))
    b = int(input("315"))

    
    while b != 0:
        a, b = b, a % b
        print(b)

except ValueError:
    print("エラー: 数値を入力してください。")



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

# 互いに素
def are_coprime(a, b):
    return gcd(a, b) == 1

# 使用例
a = 15
b = 28

if are_coprime(a, b):
    print(f"{a} と {b} は互いに素です。")
else:
    print(f"{a} と {b} は互いに素ではありません。")