tt = 'hello'

list1 = [1, 4, tt, 3.4, "yes", [1, 2]]  # 定义一个涵盖各种类型的list
print(list1, id(list1))  # 将其内容及地址打印出来[1, 4, 'hello', 3.4, 'yes', [1, 2]]  2459221516936

#  比较list中添加元素的几种方法的区别
list3 = [6, 7]  # 定义list3作为后面拼接实验使用

l2 = list1 + list3  # 使用+将list1与list3连接在一起，得到l2
print(l2, id(l2))  # 输出l2的内容及地址[1, 4, 'hello', 3.4, 'yes', [1, 2], 6, 7] 2030416995656

l2 = list1.extend(list3)  # 使用extend将list1与list3连接在一起，得到l2
print(l2, id(l2))  # 输出l2的内容及地址 None 140720980315360
print(list1, id(list1))  # 将list1内容及地址打印出来 [1, 4, 'hello', 3.4, 'yes', [1, 2], 6, 7] 2300695765640

l2 = list1.append(list3)  # 使用append将list3追加到list1中，得到l2
print(l2, id(l2))  # 输出l2的内容及地址 None 140720980315360
print(list1, id(list1))  # 将list1内容及地址打印出来 [1, 4, 'hello', 3.4, 'yes', [1, 2], 6, 7, [6, 7]] 1813342020232

# 删除操作
print(list1, id(list1))  # 输出list1的内容及地址[1, 4, 'hello', 3.4, 'yes', [1, 2], 6, 7, [6, 7]]

del list1[2:5]  # 删除list1的切片
print(list1, id(list1))  # 再次输出list1的内容及地址 [1, 4, [1, 2], 6, 7, [6, 7]]

del list1[2]  # 删除list1的索引
print(list1, id(list1))  # 再次输出list1的内容及地址

l2 = list1
print(id(l2), id(list1))  # 打印地址

del list1  # 删除list1变量
print(l2)  # l2还能访问，表明地址指向的数据并没有删除
#  print(list1)  # 再次输出list1的内容及地址 NameError: name 'list1' is not defined

l3 = l2
del l2[:]  # 删除l2全部内容
print(l2)  # 输出l2的内容及地址[]
print(l3)  # 输出l3的内容及地址也为[]，表明数据已经被删