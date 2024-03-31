#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
# https://leetcode.cn/problems/perfect-squares/description/
#
# algorithms
# Medium (66.69%)
# Likes:    1945
# Dislikes: 0
# Total Accepted:    500.8K
# Total Submissions: 750.7K
# Testcase Example:  '12'
#
# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
#
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11
# 不是。
#
#
#
# 示例 1：
#
#
# 输入：n = 12
# 输出：3
# 解释：12 = 4 + 4 + 4
#
# 示例 2：
#
#
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9
#
#
# 提示：
#
#
# 1 <= n <= 10^4
#
#
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        # 预先计算所有可能的平方数
        # square_nums = [i**2 for i in range(1, int(n**0.5)+1)]

        # dp = [float('inf')] * (n + 1)
        # dp[0] = 0
        # for i in range(1, n + 1):
        #     for square in square_nums:
        #         if i < square:
        #             break
        #         # dp[i] = min(dp[i], dp[i - square] + 1)
        #         if dp[i - square] + 1 < dp[i]:
        #             dp[i] = dp[i - square] + 1
        # return dp[n]

        # # 动态规划v1
        # # dp[i]: 到达i时的最少数量
        # dp = [0] + [1] + [float('inf') for _ in range(n-1)] # math.inf
        # for i in range(2, n+1):
        #     for j in range(1, int(i**0.5)+1): # <= n 的所有完全平方数
        #         # dp[i] = min(dp[i], dp[i-j*j]+1)
        #         if dp[i-j*j]+1 < dp[i]:
        #             dp[i] = dp[i-j*j]+1
        # return dp[-1]

        # 生成完全平方数列表
        squares = [i * i for i in range(1, int(n**0.5) + 1)]

        # 初始化队列和访问列表
        queue = deque([(n, 0)])
        visited = set([n])

        while queue:
            num, steps = queue.popleft()
            # 尝试每个完全平方数
            for square in squares:
                next_num = num - square
                # 找到目标值
                if next_num == 0:
                    return steps + 1
                # 将下一个数加入队列和访问列表
                if next_num > 0 and next_num not in visited:
                    queue.append((next_num, steps + 1))
                    visited.add(next_num)

        return -1  # 如果没有找到解，则返回 -1

# @lc code=end
