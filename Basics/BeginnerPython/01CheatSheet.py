"""
变量 和 字符串
"""
print("hello world")

msg = "hello world"
print(msg)

first_name = 'albert'
last_name = 'einstein'
full_name = first_name + ' ' + last_name
print(full_name)

"""
Lists
"""
# 创建一个list
bikes = ['trek', 'redline', 'giant']

# 获取list的第一个item
first_bike = bikes[0]
print(first_bike)
# 获取list的最后一个item
last_bike = bikes[-1]
print(last_bike)

# 循环list
for bike in bikes:
    print("Looping through a list: "+bike)

# 添加item到一个list中
bikes = []
bikes.append('trek_bike')
bikes.append('redline_bike')
bikes.append('giant_bike')

for bike in bikes:
    print(bike)

# 创建一个数字list
squares = []
for x in range(1, 11):
    squares.append(x ** 2)

for numerical in squares:
    print(numerical)

# List(cont.)
squares = [x ** 2 for x in range(1, 11)]

for numerical in squares:
    print(numerical)

finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[:2]
print(first_two)

# 复制一个list
copy_of_bikes = bikes[:]
for bike in copy_of_bikes:
    print(bike)

"""
Tuples : 元组和list类似，但是元组中的item不能被修改
"""
dimensions = (1920, 1080)
print(dimensions)

"""
 if 条件语句
"""
# 检验条件
x == 42
x != 42
x > 42
x >= 42
x < 42
x <= 42

# 带list的条件检验
'trek_bike' in bikes
'surly_bike' not in bikes

# 分配布尔值
game_active = True
can_edit = False

# 一个简单的if检验
age = 29
if age >= 18:
    print("you can vote! ")

# if-elif-else 声明
age = 12

if age < 4:
    ticket_price = 0
elif age < 18:
    ticket_price = 10
else:
    ticket_price = 15

print(ticket_price)

"""
字典 :字典存储信息片段之间的联系。字典中的每一项都是键值对
"""

# 一个简单的字典
alien = {'color': 'green', 'points': 5}
# 访问一个值
print("The alien's color is " + alien['color'])
# 添加一个新的键值对
alien['x_position'] = 0

# 循环所有的键值对
fav_numbers = {'eric': 17, 'ever': 4}
for name, number in fav_numbers.items():
    print(name + ' loves ' + str(number))

# 循环所有的键
fav_numbers = {'eric': 17, 'ever': 4}
for name in fav_numbers.keys():
    print(name + ' loves a number')

# 循环所有的值
fav_numbers = {'eric': 17, 'ever': 4}
for number in fav_numbers.values():
    print(str(number) + ' is a favorite')

"""
用户输入:你的程序可以提示用户输入。所有的输入都存储为字符串
"""
# 提示输入值
name = input("What's your name?")
print("Hello, " + name + "!")

# 数字输入提示
age = input("How old are you ?")
age = int(age)
print(age)

pi = input("What's the value of pi?")
pi = float(pi)
print(pi)