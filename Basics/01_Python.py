"""
    1   变量
"""

x = 5
print(x)

x = "hello"
print(x)

a = 1
b = 2
c = a + b
print(c)

x = 5
print(x)
print(type(x))

x = 5.0
print(x)
print(type(x))

x = True
print(x)
print(type(x))

a = 5
b = 3
print(a + b)
# 8

a = "5"
b = "3"
print(a + b)
# 53


"""
    2   Lists
"""
list_x = [3, "hello", 1]
print(list_x)

# 追加数据
list_x.append(7)
print(list_x)

print("list_x[0]:", list_x[0])
print("list_x[1]:", list_x[1])
print("list_x[2]:", list_x[2])
print("list_x[3]:", list_x[3])

print("\n")

print("list_x[-1]:", list_x[-1])  # 最后一项数据
print("list_x[-2]:", list_x[-2])  # 倒数第二项数据
print("list_x[-3]:", list_x[-3])  # 倒数第三项数据
print("list_x[-4]:", list_x[-4])  # 倒数第四项数据

print("\n")

# 切片
print("list_x[:]:", list_x[:])
print("list_x[2:]:", list_x[2:])
print("list_x[1:3]:", list_x[1:3])

print("\n")

print("list_x length：", len(list_x))  # list的长度

list_x[1] = "hi"  # 替换list中某一项
print(list_x)

list_y = [2.4, "world"]
list_z = list_x + list_y  # 列表组合
print(list_z)

print("\n")

"""
    3   Tuple
"""

tuple_x = (3.0, "hello")
print(tuple_x)

tuple_x = tuple_x + (5.6,)  # 添加一个值到一个tuple里面去
print(tuple_x)

#  tuple_x[1] = "world"
#  #不能试图改变一个tuple的值
print(tuple_x[1])  # 获取tuple中的某一项

print("\n")

"""
    4   Dictionaries
"""

goku = {"name": "Goku", "eye_color": "brown"}
print(goku)

print(goku["name"])
print(goku["eye_color"])

#  通过一个key修改字典的值
goku["eye_color"] = "green"
print(goku)

#  添加一个新的键值对
goku["age"] = 24
print(goku)

#  字典的长度
print(len(goku))


"""
    5 if 
"""

x = 4
if x < 1:
    score = "low"
elif x <= 4:
    score = "medium"
else:
    score = "high"
print(score)

print("\n")

x = True
if x:
    print("it worked")

print("\n")

"""
    6 loops 循环 
"""

#  for 循环
x = 1
for i in range(3):
    x += 1
    print("i={0}, x={1}".format(i, x))

#  while 循环
x = 3
while x > 0:
    x -= 1
    print(x)


"""
    7   函数  [函数是模块化可重用代码片段的一种方法]
"""


#  创建一个函数
def add_two(x):
    x += 2
    return x


#  使用这个函数
score = 0
score = add_two(score)
print(score)

print("\n")


def join_name(first_name, last_name):
    joined_name = first_name + " " + last_name
    return joined_name


first_name = "hou"
last_name = "jingru"
joined_name = join_name(first_name, last_name)
print(joined_name)

print("\n")

"""
    8   类
"""


#  创建一个类
class Pets(object):

    # 初始化这个类
    def __init__(self, species, color, name):
        self.species = species
        self.color = color
        self.name = name

    # 打印
    def __str__(self):
        return "{0} {1} named {2}.".format(self.color, self.species, self.name)

    # 函数示例
    def change_name(self, new_name):
        self.name = new_name


#   创建一个类的实例
my_dog = Pets(species="dog", color="orange", name="Guiness",)
print(my_dog)
print(my_dog.name)

my_dog.change_name(new_name="Charlie")
print(my_dog)
print(my_dog.name)