#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#
# https://leetcode.cn/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (53.34%)
# Likes:    1416
# Dislikes: 0
# Total Accepted:    423K
# Total Submissions: 792.3K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n' +  '5'
#
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
#
#
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
#
#
#
#
# 示例 1：
#
#
# 输入：matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 5
# 输出：true
#
#
# 示例 2：
#
#
# 输入：matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 20
# 输出：false
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -10^9 <= matrix[i][j] <= 10^9
# 每行的所有元素从左到右升序排列
# 每列的所有元素从上到下升序排列
# -10^9 <= target <= 10^9
#
#
#
from typing import List
from typing import Optional
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      #TODO 看看其他解法
      i, j = 0, 0  # 指示当前位置的行和列的索引
      row = len(matrix)  # 获取矩阵的行数
      col = len(matrix[0])  # 获取矩阵的列数
      flag = True  # 标记当前遍历的方向 True：向右遍历 False：向下遍历
      while -1 < i < row and -1 < j < col:  # 当行索引和列索引在有效范围内时
          if matrix[i][j] == target:  # 如果当前位置的值等于目标值
              return True  # 返回True
          elif matrix[i][j] < target:  # 如果当前位置的值小于目标值
              if j != col - 1 and flag:  # 如果列索引不是最后一列且标记为向右遍历
                  j += 1  # 列索引加1
              else:  # 否则
                  i += 1  # 行索引加1
                  flag = True  # 标记为向右遍历
          else:  # 如果当前位置的值大于目标值
              j -= 1  # 列索引减1
              flag = False  # 标记为向左遍历
      return False  # 如果遍历结束仍未找到目标值，则返回False

      # # 恩找
      # for row in matrix:
      #   for i in row:
      #     if i == target:
      #       return True
      # return False
# @lc code=end
solution = Solution()
# print(solution.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
# print(solution.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))
# print(solution.searchMatrix([
#                             [1,2,3,4,5],
#                             [6,7,8,9,10],
#                             [11,12,13,14,15],
#                             [16,17,18,19,20],
#                             [21,22,23,24,25]
#                             ], 19))
