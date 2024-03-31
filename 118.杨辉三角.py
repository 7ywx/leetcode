#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode.cn/problems/pascals-triangle/description/
#
# algorithms
# Easy (75.77%)
# Likes:    1141
# Dislikes: 0
# Total Accepted:    500.1K
# Total Submissions: 660K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
#
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
#
#
#
#
#
# 示例 1:
#
#
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
#
# 示例 2:
#
#
# 输入: numRows = 1
# 输出: [[1]]
#
#
#
#
# 提示:
#
#
# 1
#
#
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        res = [[1]]
        while len(res) < numRows:
            newRow = [a+b for a, b in zip([0]+res[-1], res[-1]+[0])]
            res.append(newRow)
        return res

        dp =[[1]]
        for row in range(1,numRows):
            dp.append([])
            for col in range(row+1):
                if col == 0 or col == row:
                    dp[row].append(1)
                else:
                    dp[row].append(dp[row-1][col-1]+dp[row-1][col])
        return dp
# @lc code=end
