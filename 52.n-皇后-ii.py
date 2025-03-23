#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N 皇后 II
#
# https://leetcode.cn/problems/n-queens-ii/description/
#
# algorithms
# Hard (82.43%)
# Likes:    527
# Dislikes: 0
# Total Accepted:    162.5K
# Total Submissions: 197K
# Testcase Example:  '4'
#
# n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。
#
#
#
#
#
# 示例 1：
#
#
# 输入：n = 4
# 输出：2
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#
#
# 示例 2：
#
#
# 输入：n = 1
# 输出：1
#
#
#
#
# 提示：
#
#
# 1 <= n <= 9
#
#
#
#
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        grid = [["."] * n for _ in range(n)]
        def isValid(row, col):
            # 检查同一列
            for i in range(row):
                if grid[i][col] == "Q":
                    return False
            # 检查左上
            p, q = row-1, col-1
            while p >= 0 and q >= 0:
                if grid[p][q] == "Q":
                    return False
                p -= 1
                q -= 1
            # 检查右上
            p, q = row-1, col+1
            while p >= 0 and q < n:
                if grid[p][q] == "Q":
                    return False
                p -= 1
                q += 1
            return True
        def backtracking(row):
            if row == n:
                nonlocal res
                res += 1
                return
            for col in range(n):
                if isValid(row, col):
                    grid[row][col] = "Q"
                    backtracking(row + 1)
                    grid[row][col] = "."
        backtracking(0)
        return res
# @lc code=end
