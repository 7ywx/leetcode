#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
# https://leetcode.cn/problems/n-queens/description/
#
# algorithms
# Hard (73.90%)
# Likes:    2060
# Dislikes: 0
# Total Accepted:    388.4K
# Total Submissions: 525.5K
# Testcase Example:  '4'
#
# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
#
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
#
#
#
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
#
#
# 示例 1：
#
#
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#
#
# 示例 2：
#
#
# 输入：n = 1
# 输出：[["Q"]]
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
from typing import List
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [["."] * n for _ in range(n)]
        res = []
        def dfs(grid, row):
            candidates = []
            for j in range(n):
                if grid[row][j] == ".":
                    candidates.append(j)
            if not candidates:
                return []
            for j in candidates:
                grid[row][j] = "Q"
                for n in range(j+1)
                if row == n - 1:
                    res.append(["".join(r) for r in grid])
                else:
                    dfs(grid, row + 1)
                grid[row][j] = "."
        dfs(grid, 0)
        return res
# @lc code=end
s = Solution()
print(s.solveNQueens(4))
