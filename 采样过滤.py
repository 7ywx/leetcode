# from collections import deque

# def take_sample_filter(M, T, P, samples):
#     # 下标 i -> 正常迭代下标
#     i = 0
#     n = len(samples)
#     cycle = 0
#     fail = 0

#     # 用一个栈保存正常数据的下标
#     deque_normal = deque()

#     while i < n:
#         # 判断是否进入故障恢复期
#         if cycle <= M:
#             if fail == T:
#                 # 进入恢复周期
#                 count = P
#                 while count > 0 and i < n:
#                     if judge(samples, i):
#                         count = P  # 仍然是错误数据，重新计算恢复周期
#                     else:
#                         count -= 1
#                     i += 1
#                 # 数据恢复正常后重置
#                 cycle = fail = 0
#                 continue
#             if cycle == M:
#                 # 进入下一个周期
#                 cycle = fail = 0
#                 continue

#         # 判断数据是否采样错误
#         if judge(samples, i):
#             # 故障次数 +1
#             fail += 1
#             # 数据故障，判断是否可以被近似正常值代替
#             if deque_normal:
#                 samples[i] = samples[deque_normal[0]]
#                 deque_normal.appendleft(i)
#         else:
#             # 如果是正确采样数据的话，保存下标
#             deque_normal.appendleft(i)

#         # 周期数 +1
#         cycle += 1
#         i += 1

#     # 计算最长连续正常周期
#     ans = 0
#     last_index = deque_normal.pop()
#     temp = 1
#     while deque_normal:
#         if deque_normal[0] + 1 == last_index:
#             temp += 1
#             last_index = deque_normal.pop()
#         else:
#             ans = max(ans, temp)
#             last_index = deque_normal.pop()
#             temp = 1

#     return temp if ans == 0 else ans

# def judge(samples, i):
#     # 判断是否为错误采样数据
#     return samples[i] <= 0 or (i >= 1 and samples[i] < samples[i - 1]) or samples[i] - samples[i - 1] >= 10


# # 测试用例
# M = 10
# T = 6
# P = 3
# samples = [-1, 1, 2, 3, 100, 10, 13, 9, 10]
# print("最长连续正常周期:", take_sample_filter(M, T, P, samples))
from collections import deque

def take_sample_filter(M, T, P, samples):
    # 下标 i -> 正常迭代下标
    i = 0
    n = len(samples)
    cycle = 0
    fail = 0

    # 用一个栈保存正常数据的下标
    deque_normal = deque()

    while i < n:
        # 判断是否进入故障恢复期
        if cycle <= M:
            if fail == T:
                # 进入恢复周期
                count = P
                while count > 0 and i < n:
                    if judge(samples, i):
                        count = P  # 仍然是错误数据，重新计算恢复周期
                    else:
                        count -= 1
                    i += 1
                # 数据恢复正常后重置
                cycle = fail = 0
                continue
            if cycle == M:
                # 进入下一个周期
                cycle = fail = 0
                continue

        # 判断数据是否采样错误
        if judge(samples, i):
            # 故障次数 +1
            fail += 1
            # 数据故障，判断是否可以被近似正常值代替
            if deque_normal:
                samples[i] = samples[deque_normal[0]]
                deque_normal.appendleft(i)
        else:
            # 如果是正确采样数据的话，保存下标
            deque_normal.appendleft(i)

        # 周期数 +1
        cycle += 1
        i += 1

    # 计算最长连续正常周期
    ans = 0
    last_index = deque_normal.pop()
    temp = 1
    while deque_normal:
        if deque_normal[0] + 1 == last_index:
            temp += 1
            last_index = deque_normal.pop()
        else:
            ans = max(ans, temp)
            last_index = deque_normal.pop()
            temp = 1

    return temp if ans == 0 else ans

def judge(samples, i):
    # 判断是否为错误采样数据
    return samples[i] <= 0 or (i >= 1 and samples[i] < samples[i - 1]) or samples[i] - samples[i - 1] >= 10


# 测试用例
M = 10
T = 6
P = 3
samples = [-1, 1, 2, 3, 100, 10, 13, 9, 10]
print("最长连续正常周期:", take_sample_filter(M, T, P, samples))
