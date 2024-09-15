import random
import matplotlib.pyplot as plt
import numpy as np

# 生成实验结果
res = []
i = 0
while i < 50000000:
    p = 0.01
    n = 0
    p_t = random.random()
    flag = False
    if p_t < p:
        res.append(n)
        i += 1
    else:
        while not flag:
            n += 1
            p += 0.01
            p_t = random.random()
            if p_t < p:
                flag = True
        res.append(n)
        i += 1

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号

# 计算概率分布
unique_values, counts = np.unique(res, return_counts=True)
probabilities = counts / len(res)

# 创建 x 轴的数据
x = unique_values

# 绘制概率分布曲线
plt.plot(x, probabilities, label='概率分布', color='blue', marker='o', linestyle='-')

# 标注最大值点
max_prob_index = np.argmax(probabilities)
max_prob_value = probabilities[max_prob_index]
max_x_value = unique_values[max_prob_index]

plt.plot(max_x_value, max_prob_value, 'ro')  # 红色标记最大值点
plt.text(max_x_value, max_prob_value + 0.001, f'最大值: {max_x_value} ({max_prob_value:.4f})', fontsize=10, ha='center')

# 标注最小值点
min_prob_index = np.argmin(probabilities)
min_prob_value = probabilities[min_prob_index]
min_x_value = unique_values[min_prob_index]

plt.plot(min_x_value, min_prob_value, 'go')  # 绿色标记最小值点
plt.text(min_x_value, min_prob_value - 0.001, f'最小值: {min_x_value} ({min_prob_value:.4f})', fontsize=10, ha='center')

# 设置标题和标签
plt.title('实验结果的概率分布')
plt.xlabel('n值')
plt.ylabel('概率')

# 添加图例
plt.legend()

# 显示网格
plt.grid(True)

# 显示图形
plt.show()
