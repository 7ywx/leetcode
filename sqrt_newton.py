import matplotlib.pyplot as plt
import numpy as np

def sqrt_newton_method(number, epsilon=1e-6):
    if number < 0:
        raise ValueError("输入的数值必须是非负的")

    guesses = [number]  # 存储每次迭代的猜测值
    while abs(guesses[-1] * guesses[-1] - number) > epsilon:
        new_guess = (guesses[-1] + number / guesses[-1]) / 2.0 # 关键是这
        guesses.append(new_guess)

    return guesses

# # 画图示意
# def plot_sqrt_iterations(x, guesses):
#     plt.plot(guesses, label='Guesses', marker='o')
#     plt.axhline(np.sqrt(x), color='red', linestyle='--', label='True Square Root')
#     plt.xlabel('Iterations')
#     plt.ylabel('Guess Value')
#     plt.title(f'Newton Method to Find Square Root of {x}')
#     plt.legend()
#     plt.show()

# # 示例用法
# number = 4
# guesses = sqrt_newton_method(number)
# plot_sqrt_iterations(number, guesses)

def func(x: int, number):
    return x**2 - number

def func_list(guesses: list, number) -> list:
    func_values = []
    for guess in guesses:
        func_values.append(func(x=guess, number=number))
    return func_values
def derivative(x): # 导数
    return 2 * x

def tangent_line(x_0, X, number): # 切线 X:自变量 x_0:切点横坐标 func(x_0, number):切点纵坐标
    return derivative(x_0) * (X - x_0) + func(x_0, number)

def plot_newton_iterations(number, guesses):
    x_values = np.linspace(0, max(guesses), 100) # 生成自变量 max(guesses[-1], np.sqrt(number)) + 1 func_list(guesses=guesses, number=number)
    func_values = func(x_values, number) # 生成函数值


    plt.plot(x_values, func_values, label=f'Function: $x^2 - {number}$')

    for index, guess in enumerate(guesses):
        tangent_values = tangent_line(guess, x_values, number)
        plt.plot(x_values, tangent_values, label=f'Tangent{index+1} at $y={guess:.4f}$')

    plt.axhline(0, color='black', linewidth=0.5, linestyle='--', label='y-axis') # axes horizontal line 水平参考线
    plt.axvline(np.sqrt(number), color='red', linestyle='--', label='True Square Root') # axes vertical line 垂直参考线

	# plt.figure(figsize=(8, 6))  # 设置图形大小

    # # 设置x轴和y轴的步长
    # max_func_value = max(func_values)
    # plt.xticks(np.arange(0, max(guesses) + 1, 1))
    # plt.yticks(np.arange(-np.abs(max_func_value), np.abs(max_func_value) + 1, 1))

    plt.xlabel('y') # x轴标签
    plt.ylabel('f(y)') # y轴标x
    plt.title(f'Newton Method to Find Square Root of {number}') # 设置图表标题
    plt.legend() # 图例
    plt.show()

# 示例用法
number = 98
guesses = sqrt_newton_method(number)
# plot_newton_iterations(number, guesses)
print(guesses)
