import platform
import sys
import os


def showENV():
    s = platform.platform()
    print("当前系统：", s)
    p = sys.path
    print("当前安装路径：", p)
    op = os.getcwd()
    print("当前代码流经：", op)
    print("Pythonb版本信息：", sys.version_info)


if __name__=='__main__':
    showENV()