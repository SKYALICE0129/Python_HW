# 1. 迴圏的練習-factor
# 輸入一正整數，求其所有的因數。
# 因數的定義: a * b = c

number = int(input("請輸入一個正整數:"))

for a in range(1, number+1):
    if number % a == 0:
        print(a, "\t", end="")
    else:
        continue

# 2.迴圏的練習-perfect_number
# 一個數字若等於其所有因數的總和，則此數為perfect number。
# 找出100以內所有的完美數。
# 說明：6的因數為1, 2, 3，6=1+2+3，故6為完美數。

for i in range(1, 100+1):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if i == sum:
        print(i)

# 3.迴圏的練習-Amstrong數是指一個三位數的整數，其個位數之立方和等於該數本身。
# 找出所有的Amstrong數。
# 說明：153=1^3+5^3+3^3，故153為Amstrong數。
# Amstrong = (A//100)*100+(A%100//10)*10+(A%100%10)*1

for A in range(100, 1000):
    Amstrong = (A // 100)**3 + (A % 100 // 10)**3 + (A % 100 % 10)**3
    if A == Amstrong:
        print(A)

# 4.迴圈的練習-prime
# 輸入一正整數，找出所有小於或等於的質數。
# 質數的定義:大於1的自然數中，除了1跟本身沒有其他因數

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:  # 整除，i 是 n 的因數，所以 n 不是質數。
            return False

    return True  # 都沒有人能整除，所以 n 是質數

n = int(input("請輸入一個正整數:"))

for i in range(2, n+1):  # 產生 2 到 n 的數字。
    i_is_prime = is_prime(i)
    if i_is_prime:   # 判斷 i 是否為質數，如果是True印出來
        print(i)

# 5.迴圈敘述的練習-interest
# 某人A以10%單利投資100000元，某人B則以5%複利投資100000元。計算多少年後某人B的投資可以超過某人A，並將此時兩人錢數印出。(27年後)
# 提示：單利公式：P(1+r*n)    複利公式：P(1+r)^n
# P：本金，r：利率，n：多少年

n = 1
while n > 0:
    A_SUM = 100000*(1 + 0.1 * n)
    B_SUM = 100000*(1 + 0.05)**n
    if A_SUM >= B_SUM:
        n += 1
    else:
        print(n, "年後，B的投資金額超越A:")
        print("A的投資金額 =", A_SUM)
        print("B的投資金額 =", B_SUM)
        break

