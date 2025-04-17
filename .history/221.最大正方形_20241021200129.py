from typing import List
#
# @lc app=leetcode.cn id=221 lang=python3
# @lcpr version=20002
#
# [221] 最大正方形
#
# https://leetcode.cn/problems/maximal-square/description/
#
# algorithms
# Medium (50.83%)
# Likes:    1714
# Dislikes: 0
# Total Accepted:    353.2K
# Total Submissions: 694.5K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
#
#
#
# 示例 1：
#
# 输入：matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：4
#
#
# 示例 2：
#
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
#
#
# 示例 3：
#
# 输入：matrix = [["0"]]
# 输出：0
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] 为 '0' 或 '1'
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        flag = True

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                maxLen = 1
                # row, col = i, j
                while i+maxLen < m and j+maxLen < n and flag:
                    for y in range(j, j+maxLen+1):
                        if matrix[i+maxLen][y] == '0':
                            maxLen -= 1
                            flag = False
                            break
                    if not flag:
                        # flag = True
                        break
                    for x in range(i, i+maxLen+1):
                        if matrix[x][j+maxLen] == '0':
                            maxLen -= 1
                            break
                    maxLen += 1
                if maxLen > ans: ans = maxLen
        print(ans)
        return ans
# @lc code=end
s = Solution()
s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])

#
# @lcpr case=start
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0","1"],["1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0"]]\n
# @lcpr case=end

#
