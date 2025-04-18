def is_lucky(num):
    # 判断一个数字是否为幸运数字
    num_str = str(num)
    for i in range(len(num_str)):
        for j in range(i + 1, len(num_str) + 1):
            if sum(map(int, num_str[i:j])) % 3 == 0:  # 判断子串之和是否为 3 的倍数
                return True
    return False

def count_lucky_in_range(L, R):
    lucky_count = [0] * (R + 1)

    # 计算每个数字是否为幸运数字
    for i in range(L, R + 1):
        lucky_count[i] = lucky_count[i - 1] + (1 if is_lucky(i) else 0)

    # 返回区间 [L, R] 内幸运数字的数量
    return lucky_count[R] - lucky_count[L - 1]

# 示例：查询区间 [L, R]
L = 2
R = 45
print(count_lucky_in_range(L, R))  # 输出区间 [L, R] 内幸运数字的总数
