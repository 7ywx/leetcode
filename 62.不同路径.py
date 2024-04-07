#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
# https://leetcode.cn/problems/unique-paths/description/
#
# algorithms
# Medium (68.12%)
# Likes:    2012
# Dislikes: 0
# Total Accepted:    764.9K
# Total Submissions: 1.1M
# Testcase Example:  '3\n7'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
#
# 问总共有多少条不同的路径？
#
#
#
# 示例 1：
#
#
# 输入：m = 3, n = 7
# 输出：28
#
# 示例 2：
#
#
# 输入：m = 3, n = 2
# 输出：3
# 解释：
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向下
#
#
# 示例 3：
#
#
# 输入：m = 7, n = 3
# 输出：28
#
#
# 示例 4：
#
#
# 输入：m = 3, n = 3
# 输出：6
#
#
#
# 提示：
#
#
# 1 <= m, n <= 100
# 题目数据保证答案小于等于 2 * 10^9
#
#
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #TODO dp还有优化空间
        # 动态规划 v1.1 对于dp的初始化进行了优化
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        #print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

        # 动态规划 v1
        dp = [[0 for _ in range(n)] for _ in range(m)] # 到达(m, n)的路径有几条
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

        # 回溯 超时
        dp = [[0 for _ in range(n)] for _ in range(m)] # 到达(m, n)的路径有几条
        dp[0][0] = 1

        # direction 0: down 1:right
        def dfs(i, j):
            if i == m-1 and j == n-1:
                return

            original = (i, j)
            direction = []
            if i < m-1:
                direction.append(0)
            if j < n-1:
                direction.append(1)
            for d in direction:
                if d == 0:
                    if dp[i+1][j] == 0:
                        dp[i+1][j] = dp[i][j]
                    else:
                        dp[i+1][j] += 1 #dp[i][j]
                    dfs(i+1, j)
                    i = original[0]
                    j = original[1]
                else:
                    if dp[i][j+1] == 0:
                        dp[i][j+1] = dp[i][j]
                    else:
                        dp[i][j+1] += 1 #dp[i][j]
                    dfs(i, j+1)
                    i = original[0]
                    j = original[1]
        dfs(0, 0)
        return dp[m-1][n-1]
# @lc code=end
s = Solution()
print(s.uniquePaths(3, 3))
