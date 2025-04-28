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
        nums = [i  for i in range(n)]
        path = [-1] * n
        ans = []
        m = 2 * n - 1
        diag1 = [False] * m
        diag2 = [False] * m
        def dfs(i, s):
            if i == n:
                ans.append(['.'*c + 'Q' + '.' * (n-1-c) for c in path])
                return
            for c in s:
                # if all(i+c != R+path[R] and i-c != R - path[R] for R in range(i)):
                if not diag1[i+c] and not diag2[i-c]:
                    diag1[i+c] = diag2[i-c] = True
                    path[i] = c
                    dfs(i+1, s-{c})
                    diag1[i+c] = diag2[i-c] = False
        dfs(0, set(nums))
        return ans

        grid = [["."] * n for _ in range(n)]
        res = []
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
        def backtrack(row):
            # 如果到最后一行了，则将结果添加到res里
            if row == n:
                tmp = [''.join(i) for i in grid]
                res.append(tmp)
                return

            for col in range(n):
                if not isValid(row, col):
                    continue
                grid[row][col] = 'Q'
                backtrack(row + 1)
                grid[row][col] = '.'
        # backtrack(0)
        dfs(0)
        return res
# @lc code=end
s = Solution()
print(s.solveNQueens(100))
