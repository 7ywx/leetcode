
# stack = []

# # 检查变量是否为 None
# if stack is not None:
#     print("stack 不为 None")
# else:
#     print("stack 为 None")

# # 定义 ANSI 转义码
# RESET = "\033[0m"  # 重置颜色
# RED = "\033[0;31m"  # 红色

# # 原始字符串
# text = "Hello world"

# # 指定要突出显示的字符位置
# i = 4  # 例如，突出显示第6个字符（索引为5）

# # 构造突出显示的字符串
# highlighted_text = text[:i] + RED + text[i] + RESET + text[i+1:]

# # 打印突出显示的字符串
# print(highlighted_text)
# print("\033[0;31;44mHello world!\033[0m")  # 不高亮，红字，蓝底
# print("\033[1;31;40mHello world!\033[0m")  # 高亮，红字，黑底


import time
# def decorator1(func):
#     """
#     第一个装饰器，打印 "Decorator 1 starts."
#     """
#     def wrapper(*args, **kwargs):
#         print("Decorator 1 starts.")
#         return func(*args, **kwargs)
#     return wrapper

# def decorator2(func):
#     """
#     第二个装饰器，打印 "Decorator 2 starts."
#     """
#     def wrapper(*args, **kwargs):
#         print("Decorator 2 starts.")
#         return func(*args, **kwargs)
#     return wrapper

# @decorator1
# @decorator2
# def example_function():
#     """
#     示例函数，输出 "Function starts."
#     """
#     print("Function starts.")

# # 调用被多个装饰器修饰后的函数
# example_function()
# def repeat(num_times):
#     """
#     重复执行指定次数的装饰器。

#     参数：
#     num_times -- 重复次数
#     """
#     def decorator_repeat(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeat

# @repeat(num_times=3)
# def example_function():
#     """
#     示例函数，简单打印一条消息。
#     """
#     print("Hello, world!")

# # 调用带参数的装饰器修饰后的函数
# example_function()
# import heapq
# h=[2,3,4,1,-1]
# print(heapq.heappop(h))

# if 4 ^ 1 == ~4:
#     print(1)

n = 2**30 # int(input())

import cmath  # 为了处理可能出现的复数解
import math
def solve_quadratic(a, b, c):
    # 计算判别式
    delta = b**2 - 4 * a * c

    # 计算两个解
    root1 = (-b - cmath.sqrt(delta)) / (2 * a)
    root2 = (-b + cmath.sqrt(delta)) / (2 * a)

    # 如果判别式大于等于0，解是实数
    if delta >= 0:
        root1 = root1.real
        root2 = root2.real

    return (root1, root2)

right = math.ceil(n / 2)
left = math.ceil(solve_quadratic(1, 1, -n*2)[1])
print(right, left)
