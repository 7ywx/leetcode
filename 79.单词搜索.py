#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode.cn/problems/word-search/description/
#
# algorithms
# Medium (46.76%)
# Likes:    1793
# Dislikes: 0
# Total Accepted:    502.6K
# Total Submissions: 1.1M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#
#
# 示例 1：
#
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "ABCCED"
# 输出：true
#
#
# 示例 2：
#
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "SEE"
# 输出：true
#
#
# 示例 3：
#
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "ABCB"
# 输出：false
#
#
#
#
# 提示：
#
#
# m == board.length
# n = board[i].length
# 1
# 1
# board 和 word 仅由大小写英文字母组成
#
#
#
#
# 进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？
#
#
from typing import List, Optional
# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def fund(target, i, j):
            res = []
            if i == -1 and j == -1:
                for i in range(len(board)):
                    for j in range(len(board[0])):
                        if board[i][j] == target:
                            res.append((i, j))
                return res
            else:
                if i > 0 and board[i - 1][j] == target:
                    res.append((i - 1, j))
                if j > 0 and board[i][j - 1] == target:
                    res.append((i, j - 1))
                if i < len(board) - 1 and board[i + 1][j] == target:
                    res.append((i + 1, j))
                if j < len(board[0]) - 1 and board[i][j + 1] == target:
                    res.append((i, j + 1))
                return res
        # def near(i, j, target):
        #     res = []
        #     if i > 0 and board[i - 1][j] == target:
        #         res.append((i - 1, j))
        #     if j > 0 and board[i][j - 1] == target:
        #         res.append((i, j - 1))
        #     if i < len(board) - 1 and board[i + 1][j] == target:
        #         res.append((i + 1, j))
        #     if j < len(board[0]) - 1 and board[i][j + 1] == target:
        #         res.append((i, j + 1))
        #     return res
        def dfs(i, j, k):
            # if k == 0:
            #     first = fund(word[k])
            #     if not first:
            #         return False
            #     for x, y in first:
            #         board[x][y] = '#'
            #         if not dfs(x, y, k + 1):
            #             board[x][y] = word[k]
            # elif k < len(word):
            #     near = near(i, j, word[k])
            #     if not near:
            #         return False
            #     for x, y in near:
            #         board[x][y] = '#'
            #         if not dfs(x, y, k + 1):
            #             board[x][y] = word[k]
            # elif k == len(word):
            #     return True
            if k == len(word):
                return True
            else:
                near = fund(word[k], i, j)
                if not near:
                    return False
                for x, y in near:
                    board[x][y] = '#'
                    if dfs(x, y, k + 1):
                        return True
                    board[x][y] = word[k]
                    # board[x][y] = '#'
                    # if dfs(x, y, k + 1):
                    #     return True
                    # board[x][y] = word[k]
                return False
        return dfs(-1, -1, 0)

# @lc code=end
s = Solution()
# print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
# print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
