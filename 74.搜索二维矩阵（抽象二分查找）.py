#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#
# https://leetcode.cn/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (49.46%)
# Likes:    907
# Dislikes: 0
# Total Accepted:    382.9K
# Total Submissions: 774.2K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# 给你一个满足下述两条属性的 m x n 整数矩阵：
#
#
# 每行中的整数从左到右按非严格递增顺序排列。
# 每行的第一个整数大于前一行的最后一个整数。
#
#
# 给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
#
#
# 示例 2：
#
#
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
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
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4
#
#
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        matrix_len = row * col

        # 开区间
        left, right = -1, matrix_len # (-1, matrix_len)
        while left + 1 < right: # 区间不为空
            mid = (left + right) // 2
            mid_value = matrix[mid // col][mid % col]
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid
            else:
                right = mid
        return False

        # 左闭右开
        left, right = 0, matrix_len # [0, matrix_len)
        while left < right: # 区间不为空
            mid = (left + right) // 2
            mid_value = matrix[mid // col][mid % col]
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid
        return False

        # 闭区间
        left, right = 0, matrix_len - 1
        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // col][mid % col]
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
# @lc code=end
