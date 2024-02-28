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
        res = []  # 用于存储结果的列表
        row = len(matrix)  # 矩阵的行数
        col = len(matrix[0])  # 矩阵的列数
        matrix_len = row * col  # 矩阵的元素总数
        counter = 0  # 计数器，用于记录已经遍历的元素数量
        top_border = 0  # 上边界
        bottom_border = row - 1  # 下边界
        left_border = 0  # 左边界
        right_border = col - 1  # 右边界
        i = 0  # 当前元素的行索引
        j = 0  # 当前元素的列索引
        def right():  # 向右遍历矩阵
            nonlocal i, j, counter, top_border  # 使用非本地变量
            while j <= right_border:  # 当列索引小于等于右边界时
                res.append(matrix[i][j])  # 将当前元素添加到结果列表中
                counter = counter + 1  # 计数器加一
                j += 1  # 列索引加一
            i += 1  # 行索引加一
            j -= 1  # 列索引减一
            top_border += 1  # 上边界加一
        def down():  # 向下遍历矩阵
            nonlocal i, j, counter, right_border  # 使用非本地变量
            while i <= bottom_border:  # 当行索引小于等于下边界时
                res.append(matrix[i][j])  # 将当前元素添加到结果列表中
                counter = counter + 1  # 计数器加一
                i += 1  # 行索引加一
            j -= 1  # 列索引减一
            i -= 1  # 行索引减一
            right_border -= 1  # 右边界减一
        def left():  # 向左遍历矩阵
            nonlocal i, j, counter, bottom_border  # 使用非本地变量
            while j >= left_border:  # 当列索引大于等于左边界时
                res.append(matrix[i][j])  # 将当前元素添加到结果列表中
                counter = counter + 1  # 计数器加一
                j -= 1  # 列索引减一
            i -= 1  # 行索引减一
            j += 1  # 列索引加一
            bottom_border -= 1  # 下边界减一
        def up():  # 向上遍历矩阵
            nonlocal i, j, counter, left_border  # 使用非本地变量
            while i >= top_border:  # 当行索引大于等于上边界时
                res.append(matrix[i][j])  # 将当前元素添加到结果列表中
                counter = counter + 1  # 计数器加一
                i -= 1  # 行索引减一
            j += 1  # 列索引加一
            i += 1  # 行索引加一
            left_border += 1  # 左边界加一
        while counter < matrix_len:  # 当计数器小于矩阵元素总数时
            right()  # 向右遍历矩阵
            if counter == matrix_len:  # 如果计数器等于矩阵元素总数
                break  # 跳出循环
            down()  # 向下遍历矩阵
            if counter == matrix_len:  # 如果计数器等于矩阵元素总数
                break  # 跳出循环
            left()  # 向左遍历矩阵
            if counter == matrix_len:  # 如果计数器等于矩阵元素总数
                break  # 跳出循环
            up()  # 向上遍历矩阵
            if counter == matrix_len:  # 如果计数器等于矩阵元素总数
                break  # 跳出循环
        return res  # 返回结果列表
# @lc code=end
solution = Solution()
print(solution.spiralOrder([[7],[9],[6]]))
