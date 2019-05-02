birth_year = input("请输入出生年份： ")
age = 2019 - int(birth_year)
print(age)


print(type(birth_year))
print(type(age))

"""
类型转换

 int(birth_year)
 float(birth_year)
 bool(birth_year)
"""


weight = input("请输入您的体重【斤】： ")
weight_kg = int(weight) / 2.0
print(weight_kg)

print("你的体重为： " + str(weight_kg) + " 公斤")