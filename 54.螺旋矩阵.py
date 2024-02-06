#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode.cn/problems/spiral-matrix/description/
#
# algorithms
# Medium (50.11%)
# Likes:    1596
# Dislikes: 0
# Total Accepted:    456.8K
# Total Submissions: 910K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
#
# 示例 2：
#
#
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1
# -100
#
#
#
from typing import List
from typing import Optional
# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #TODO 深入理解self, nonlocal
        #TODO 优化
        res = []
        row = len(matrix)
        col = len(matrix[0])
        matrix_len = row * col
        counter = 0
        top_border = 0
        bottom_border = row - 1
        left_border = 0
        right_border = col - 1
        i = 0
        j = 0
        def right():
            nonlocal i, j, counter, top_border
            while j <= right_border:
                res.append(matrix[i][j])
                counter = counter + 1
                j += 1
            i += 1
            j -= 1
            top_border += 1
        def down():
            nonlocal i, j, counter, right_border
            while i <= bottom_border:
                res.append(matrix[i][j])
                counter = counter + 1
                i += 1
            j -= 1
            i -= 1
            right_border -= 1
        def left():
            nonlocal i, j, counter, bottom_border
            while j >= left_border:
                res.append(matrix[i][j])
                counter = counter + 1
                j -= 1
            i -= 1
            j += 1
            bottom_border -= 1
        def up():
            nonlocal i, j, counter, left_border
            while i >= top_border:
                res.append(matrix[i][j])
                counter = counter + 1
                i -= 1
            j += 1
            i += 1
            left_border += 1
        while counter < matrix_len:
            right()
            if counter == matrix_len:
                break
            down()
            if counter == matrix_len:
                break
            left()
            if counter == matrix_len:
                break
            up()
            if counter == matrix_len:
                break
        return res

        # right()
        # print('left:', i+1, j+1, matrix[i][j])
        # down()
        # print('down:', i+1, j+1, matrix[i][j])
        # left()
        # print('left:', i+1, j+1, matrix[i][j])
        # print('top_border:', top_border)
        # up()
        # print('up:', i+1, j+1, matrix[i][j])
        # right()
        # print('counter:', counter)
        # print('res:', res)
# @lc code=end
solution = Solution()
print(solution.spiralOrder([[7],[9],[6]]))
