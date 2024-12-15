#関数


E=True
m=61
def is_prime(m):
  
    if m <= 1:
        return False
    for i in range(2, m):
        if m % i == 0:
            return False
    return True
E=is_prime(m)
if E:
     print(f"{m}は素数です")
else:
     print(f"{m}は素数ではありません")

E=True
m=10
def is_prime(m):
  
    if m <= 1:
        return False
    for i in range(2, m):
        if m % i == 0:
            return False
    return True
E= is_prime(m)
if E:
     print(f"{m}は素数です")
else:
     print(f"{m}は素数ではありません")