#関数


def is_prime(m):
    if m <= 1:
        return False
    for i in range(2, int(m**0.5) + 1): 
        if m % i == 0:
            return False
    return True

# 61の判定
m = 61
if is_prime(m):
    print(f"{m}は素数です")
else:
    print(f"{m}は素数ではありません")

# 10の判定
m = 10
if is_prime(m):
    print(f"{m}は素数です")
else:
    print(f"{m}は素数ではありません")