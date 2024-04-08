#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode.cn/problems/minimum-path-sum/description/
#
# algorithms
# Medium (70.18%)
# Likes:    1661
# Dislikes: 0
# Total Accepted:    586.4K
# Total Submissions: 835.1K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
#
#
# 示例 1：
#
#
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
#
#
# 示例 2：
#
#
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
#
#
#
#
# 提示：
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200
#
#
#
from typing import List
# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid[:]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j != 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0 and i != 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                elif i == 0 and j == 0:
                    continue
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                # for m in range(len(dp)):
                #     for n in range(len(dp[0])):
                #         print(dp[m][n], end=' ')
                #     print()
                # print()
        return dp[-1][-1]
# @lc code=end
s = Solution()
print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
