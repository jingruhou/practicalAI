import platform
import sys
import os


def showOS():
    s = platform.platform()
    print("当前操作系统： ", s)


def showPath():
    p = sys.path
    print("当前安装路径: ", p)


def showCwd():
    op = os.getcwd()
    print("当前代码路径: ", op)


def showPythonInfo():
    pyInfo = sys.version_info
    print("Python版本信息： ", pyInfo)


if __name__ == '__main__':
    showOS()
    showPath()
    showCwd()
    showPythonInfo()

