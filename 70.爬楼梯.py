#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# https://leetcode.cn/problems/climbing-stairs/description/
#
# algorithms
# Easy (54.45%)
# Likes:    3481
# Dislikes: 0
# Total Accepted:    1.4M
# Total Submissions: 2.6M
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
#
#
# 示例 1：
#
#
# 输入：n = 2
# 输出：2
# 解释：有两种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶
# 2. 2 阶
#
# 示例 2：
#
#
# 输入：n = 3
# 输出：3
# 解释：有三种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶 + 1 阶
# 2. 1 阶 + 2 阶
# 3. 2 阶 + 1 阶
#
#
#
#
# 提示：
#
#
# 1 <= n <= 45
#
#
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 要到达第 n 步，您之前的步骤可能是什么？ （考虑步长）

        # 滚动数组v2
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

        # 滚动数组v1
        p, q, r = 0, 1, 1
        for _ in range(n-1):
            p = q
            q = r
            r = p + q
        return r

        # 动态规划 正着来
        # f(n) = f(n-1) + f(n-2)
        dp = [0] * (n+1)
        dp[1] = 1
        if n > 1:
            dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

        # 递归 反着来
        def getN(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            else:
                return getN(n-1) + getN(n-2)
        return getN(n)
# @lc code=end
