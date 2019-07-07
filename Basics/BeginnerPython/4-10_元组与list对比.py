#  空元素
t = ()  # 空元组
li = []  # 空list

#  一个元素的注意
t = (3)  # 一个元素的注意
t1 = (3,)  # 必须加逗号
li = [3]  # 对于list加不加都可以
l1 = [3,]  # 对于list加不加都可以
print(t, t1, li, l1)

#  元素修改处理
tt = 'hello'
t1 = (1, 3, 4, tt, 3.4, "yes", [1, 2], (4, 3))

print(t1)

t1[6][0] = "3445"
print(t1)

#  t1[0] = 3  # TypeError: 'tuple' object does not support item assignment
