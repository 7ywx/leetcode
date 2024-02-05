#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#
# https://leetcode.cn/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (65.04%)
# Likes:    1016
# Dislikes: 0
# Total Accepted:    314.5K
# Total Submissions: 482.4K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
#
#
#
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：[[1,0,1],[0,0,0],[1,0,1]]
#
#
# 示例 2：
#
#
# 输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# 输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31 - 1
#
#
#
#
# 进阶：
#
#
# 一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个仅使用常量空间的解决方案吗？
#
#
#
from typing import List
from typing import Optional
# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #TODO 记忆集合的定义和遍历
        # 初始化空行和空列
        zero_row = set()
        zero_col = set()

        # 遍历矩阵，将所有值为0的行和列添加到对应的集合中
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)

        # 将所有空行的值设置为0
        for row in zero_row:
            for j in range(len(matrix[0])):
                matrix[row][j] = 0

        # 将所有空列的值设置为0
        for col in zero_col:
            for i in range(len(matrix)):
                matrix[i][col] = 0
# @lc code=end
solution = Solution()
solution.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
