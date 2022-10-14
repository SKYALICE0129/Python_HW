# 1.函數的練習-power
# 寫一函數power(x, n)用來計算x的n次方。

def power(x, n):
    cal = x**n
    return cal

print(power(x, n))

# 2.函數的練習-is_prime
# 寫一函數is_prime(n)用來判斷n是否為質數。
# 質數定義: 一個數不能被 所有小於自己的數(不包括 1 和 自己) 整除的, 就是質數

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

n = int(input('輸入一個正整數:'))

if is_prime(n):
    print('是質數')
else:
    print('不是質數')

# 3.函數的練習- 寫一函數get_prime (n)用來找出第n個質數。

n = int(input("請輸入要找第幾個質數?")) # 输入n，表示要找第n个质数

def isprime(number):  #判断一個數是否是質数
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:  #如果有因数，則證明不是質數，返回0
            return 0
    return 1  #其他情况則證明是質數，返回1

res = 3   # 從4開始判斷, 2是第一個質數，2和3已经是質數，則n-2,
n = n - 2
while n:   #當n不為0，則證明還没找到第n個質數
    res = res + 1  #從4開始判斷，每次判斷+1
    if isprime(res):
        n = n-1
print(res)

# 4.函數的練習-mersenne_prime(梅森素數)
# 寫一函數is_mersenne_prime(n)用來判斷n是否為Mersenne質數。撰寫一程式找出前5個Mersenne質數。
# 提示：若質數滿足2^P-1=n (p為正整數)，則n為Mersenne Prime。
# 說明：當p=3時，2^3-1=7，故7為Mersenne Prime。

def is_mersenne_prime(p):
    number = 2**p-1
    for i in range(2, number):
        if number % i == 0:
            return False, number
    return True, number

data = []   # 建立空串列
n = 2       # 次方從2開始
while len(data) < 5:   # 串列長度<5，才會進入迴圈判斷
    Boolean, m_p = is_mersenne_prime(n)
    if Boolean is True:
        data.append(m_p)  # 當為梅森質數，新增質數到data=[]
    n += 1

print(data)

# 5.遞迴函數的練習-factorial_recursive
# 寫一遞迴函數factorial (n)用來計算1*2*3*…*n的值。
# 提示：factorial (n) = n * factorial(n-1)，factorial(1)=1

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

a = int(input("請輸入一個正整數?"))
print("Factorial of", a, "=", fact(a))
