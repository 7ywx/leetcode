#
# @lc app=leetcode.cn id=37 lang=python3
# @lcpr version=30200
#
# [37] 解数独
#
# https://leetcode.cn/problems/sudoku-solver/description/
#
# algorithms
# Hard (67.90%)
# Likes:    1926
# Dislikes: 0
# Total Accepted:    289.4K
# Total Submissions: 427.1K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# 编写一个程序，通过填充空格来解决数独问题。
#
# 数独的解法需 遵循如下规则：
#
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
#
#
# 数独部分空格内已填入了数字，空白格用 '.' 表示。
#
#
#
#
#
#
# 示例 1：
#
# 输入：board =
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
#
# 输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# 解释：输入的数独如上图所示，唯一有效的解决方案如下所示：
#
#
#
#
#
#
# 提示：
#
#
# board.length == 9
# board[i].length == 9
# board[i][j] 是一位数字或者 '.'
# 题目数据 保证 输入数独仅有一个解
#
#
#
#
#
#

from typing import *
# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # False：没使用，True：使用
        row = [[0]* 9 for _ in range(9)]
        col = [[0]* 9 for _ in range(9)]
        box = [[0]* 9 for _ in range(9)]

        for x in range(9):
            for y in range(9):
                if board[x][y].isdigit():
                    num = int(board[x][y]) - 1
                    boxid = (x // 3) + (y // 3) * 3
                    row[x][num] = col[y][num] = box[boxid][num] = 1

        def printBoard(board):
            for row in board:
                print(row)
            print()

        def getAvailable(x, y):
            available = [True] * 9
            boxid = (x // 3) + (y // 3) * 3
            for i in range(9):
                if row[x][i] or col[y][i] or box[boxid][i]:
                    available[i] = False
            res = []
            for i in range(9):
                if available[i]:
                    res.append(i+1)

            return res

        def backtrack(start):
            if start == 81:
                return True
            x, y = divmod(start, 9)
            if board[x][y].isdigit():
                return backtrack(start+1)
            else:
                available = getAvailable(x, y)
                if not available:
                    return False
                for possible in available:
                    board[x][y] = str(possible)
                    num = int(board[x][y]) - 1
                    boxid = (x // 3) + (y // 3) * 3
                    row[x][num] = col[y][num] = box[boxid][num] = 1
                    if not backtrack(start+1):
                        board[x][y] = "."
                        row[x][num] = col[y][num] = box[boxid][num] = 0
                    else:
                        return True
                return False

        backtrack(0)

# @lc code=end
if __name__ == '__main__':
    solution = Solution()
    board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]
    solution.solveSudoku(board)
    # your test code here



#
# @lcpr case=start
# \n[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

#
