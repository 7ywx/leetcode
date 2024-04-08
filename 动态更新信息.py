import time


# def update_output(new_content):
#     # print(f"\033[1A\033[K{new_content}", end="", flush=True)
#     print(f"\033[1G\033[K{new_content}", end="", flush=True)

# update_output("Initial content...")
# print()
# for i in range(0, 5):
#     time.sleep(1)
#     update_output(f"{i+1} seconds passed...")
#     # command = input()
#     # if command == "enter":
#     #     continue
# # update_output("Updated content...")


import os
import time
import sys

def clear():
    # 根据不同的操作系统，执行清屏操作
    os.system('cls' if os.name == 'nt' else 'clear')

def print_dp(dp):
    for row in dp:
        print(' '.join(map(str, row)))

m, n = 5, 5  # 假设dp数组的大小
dp = [[0 for _ in range(n)] for _ in range(m)]  # 初始化dp数组

for update in range(10):  # 假设有10次更新
    clear()  # 清屏
    print_dp(dp)  # 打印当前的dp数组状态

    # 更新dp数组内容的示例
    for i in range(m):
        for j in range(n):
            dp[i][j] += 1

    print("\n输入'回车'继续，输入数字则跳过该数字对应的次数更新：", end='')
    choice = input()
    if choice.isdigit():
        skip = int(choice)
        for _ in range(skip):
            for i in range(m):
                for j in range(n):
                    dp[i][j] += 1
    elif choice == "":
        continue
    else:
        print("无效输入，继续更新...")
        time.sleep(1)  # 等待1秒
