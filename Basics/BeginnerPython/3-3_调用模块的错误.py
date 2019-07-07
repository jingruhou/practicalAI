"""
    Python特性：函数调用 - 就近原则，
    调用函数时，系统会找 离 该函数 最近 代码定义 来执行
"""

#  模块函数被覆盖
from getenv import *


def showOS():
    print("(local)this is my env.")

showOS()

########################################################################################################################


#  本地函数被覆盖
def showENV():
    print("(local)this is my env.")


from getenv import *
showOS()
