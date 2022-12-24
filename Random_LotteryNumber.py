import random

number = []  # 建立一個空串列
for i in range(1, 50):
    number.append(i)  # 取1~49數字，加入空串列
# print(number)
list1 = random.sample(number, 7)   # 隨機取7個不重複號碼
special = list1.pop()  # 取最後1碼，為特別號
list1.sort()  # (將剩下數字)由小到大排序
# print(list1)
# print(special)
print("本期大樂透中獎號碼為:", end="")
for i in range(6):
    if i == 5:  # 第6個數字，後面不加逗號
        print(list1[i])
    else:  # 取前面5個數字(每取一個，後面都要加逗號)
        print(list1[i], end=",")
print("本期大樂透特別號為:", special)



# print("本期大樂透中獎號碼為:", )





