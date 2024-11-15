#制御構文
n=61
D=True
for i in range(2,n):
    if n % i ==0: 
               D=True
               break
    else :
        D=False
        

if D:
     print(f"{n}は素数ではありません")
else:
     print(f"{n}は素数です")
n=10       


D=True
for i in range(2,n):
    if n % i ==0: 
               D=True
               break
    else :
        D=False
        

if D:
     print(f"{n}は素数ではありません")
else:
     print(f"{n}は素数です")

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