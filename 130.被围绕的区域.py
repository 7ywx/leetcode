#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
# https://leetcode.cn/problems/surrounded-regions/description/
#
# algorithms
# Medium (46.72%)
# Likes:    1154
# Dislikes: 0
# Total Accepted:    302.3K
# Total Submissions: 646.5K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' 组成，捕获 所有 被围绕的区域：
#
#
# 连接：一个单元格与水平或垂直方向上相邻的单元格连接。
# 区域：连接所有 'O' 的单元格来形成一个区域。
# 围绕：如果您可以用 'X' 单元格 连接这个区域，并且区域中没有任何单元格位于 board 边缘，则该区域被 'X' 单元格围绕。
#
#
# 通过将输入矩阵 board 中的所有 'O' 替换为 'X' 来 捕获被围绕的区域。
#
#
#
#
#
# 示例 1：
#
#
# 输入：board =
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
#
# 解释：
#
# 在上图中，底部的区域没有被捕获，因为它在 board 的边缘并且不能被围绕。
#
#
# 示例 2：
#
#
# 输入：board = [["X"]]
#
# 输出：[["X"]]
#
#
#
#
# 提示：
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] 为 'X' 或 'O'
#
#
#
#
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        notArround = {}

        def infect(i, j):
            if board[i][j] == "O" and (i, j) not in notArround:
                notArround[(i, j)] = 1
                if i > 0:
                    infect(i-1, j)
                if i < m-1:
                    infect(i+1, j)
                if j > 0:
                    infect(i, j-1)
                if j < n-1:
                    infect(i, j+1)

        for i in [0, m-1] if m > 1 else [0]:
            for j in range(n):
                infect(i, j)
        for j in [0, n-1] if n > 1 else [0]:
            if m > 2:
                for i in range(1, m-1):
                    infect(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in notArround:
                    board[i][j] = "X"
# @lc code=end
