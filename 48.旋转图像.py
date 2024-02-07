#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#
# https://leetcode.cn/problems/rotate-image/description/
#
# algorithms
# Medium (75.45%)
# Likes:    1808
# Dislikes: 0
# Total Accepted:    527.3K
# Total Submissions: 698.1K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
#
# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[7,4,1],[8,5,2],[9,6,3]]
#
#
# 示例 2：
#
#
# 输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# 输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
#
#
#
#
# 提示：
#
#
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000
#
#
#
#
#
from typing import List
from typing import Optional
# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)  # 获取矩阵的行数
        if n == 1: return matrix  # 如果矩阵只有一个元素，则直接返回
        target = n//2  # 目标位置为矩阵的中间位置(change的停止条件)
        i = 0  # 初始化位置为矩阵的左上角

        """
        (0, 0) -> (0, n-1)
        (0, 1) -> (1, n-1)
        (0, n-1) -> (n-1, n-1)
        (x, y) -> (y, n-1-x)
        (0, 0) ... (0, n-2) -> (1, 1) ... -> (a,a), n=2a+1
        (0, 0) -> (a,a) ... , n=2a

        n_0 = 0
        n_2 = 1
        n_3 = 2+(n_0) = 2
        n_4 = 3+(n_2) = 4
        n_N = N-1 + n_{N-2}
        n_{N-1} = N-2 + n_{N-3}
        n_{N-2} = N-3 + n_{N-4}
        n_N = N-1 + N-3 + ... + N-(2a+1) = (a+1)N - N*N (N=2a+1, a \in {0,1,...,a})
        """
        def find_pos(x, y):  # 定义一个函数，用于计算目标位置
            return (y, n-1-x)
        def change(x, y):  # 定义一个函数，用于交换位置上的元素
            x_target, y_target = find_pos(x, y)
            x_next, y_next = find_pos(x_target, y_target)
            t, matrix[x_target][y_target] = matrix[x_target][y_target], matrix[x][y]
            while (x_next, y_next) != (x_target, y_target):
                t, matrix[x_next][y_next] = matrix[x_next][y_next], t
                x_next, y_next = find_pos(x_next, y_next)

        while i != target:  # 当 当前位置不是目标位置时，进行位置交换
            for j in range(i, n-i-1):
                change(i,j)
            i += 1
# @lc code=end
solution = Solution()
# solution.rotate([[1,2,3],[4,5,6],[7,8,9]])
solution.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
