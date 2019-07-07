# list实现队列
queue = []  # 定义一个空list，当作队列
queue.insert(0, 1)  # 向队列里放入一个整型元素 1
queue.insert(0, 2)  # 向队列里放入一个整形元素 2
queue.insert(0, "hello")  # 向队列里面放入一个字符型元素 hello

print("取第一个元素：", queue.pop())  # 从队列里面取一个元素，根据先进先出原则，输出 1
print("取第二个元素: ", queue.pop())  # 从队列里面取一个元素，根据先进先出原则，输出 2
print("取第三个元素: ", queue.pop())  # 从队列里面取一个元素，根据先进先出原则，输出 hello

#  list 实现栈
stack = []  # 定义一个空list,当作栈
stack.append(1)  # 向栈里面放入一个元素 1
stack.append(2)  # 向栈里面放入一个元素 2
stack.append("hello")  # 向栈里面放入一个元素 hello

print("取第一个元素", stack.pop())  # 从栈里面取一个元素，然后根据后进先出原则，输出 hello
print("取第二个元素", stack.pop())  # 从栈里面取一个元素，然后根据后进先出原则，输出 2
print("取第三个元素", stack.pop())  # 从栈里面取一个元素，然后根据后进先出原则，输出 1


from collections import deque

queueandstack = deque()  # 创建一个空结构体，既可以当队列又可以当栈

queueandstack.append(1)  # 向空结构体里放入一个整形元素 1
queueandstack.append(2)  # 向空结构体里放入一个整形元素 2
queueandstack.append("hello")  # 向空结构体放入一个字符型元素 hello

print(list(queueandstack))

print(queueandstack.popleft())  # 从队列里面取一个元素，根据先进先出原则，输出 1
print(queueandstack.pop())  # 从栈里面取一个元素，根据后进先出原则，输出 hello
print("Now queue is", list(queueandstack))