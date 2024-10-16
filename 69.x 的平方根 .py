from typing import List
#
# @lc app=leetcode.cn id=69 lang=python3
# @lcpr version=20001
#
# [69] x 的平方根
#
# https://leetcode.cn/problems/sqrtx/description/
#
# algorithms
# Easy (38.63%)
# Likes:    1591
# Dislikes: 0
# Total Accepted:    968.5K
# Total Submissions: 2.5M
# Testcase Example:  '4'
#
# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
#
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
#
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
#
#
#
# 示例 1：
#
# 输入：x = 4
# 输出：2
#
#
# 示例 2：
#
# 输入：x = 8
# 输出：2
# 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
#
#
#
#
# 提示：
#
#
# 0 <= x <= 2^31 - 1
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = (left + right) // 2
            if mid ** 2 > x:
                right = mid-1
            else:
                left = mid+1
        return right-1 if right**2 > x else right

        left, right = 0, x
        mid = (left + right) // 2
        while not(mid**2 <= x and (mid+1)**2 > x):
            if mid ** 2 > x:
                right = mid-1
            else:
                left = mid+1
            mid = (left + right) // 2
        return mid


        i = 0
        while not(i**2 <= x and (i+1)**2 > x):
            i += 1
        return i
# @lc code=end



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 8\n
# @lcpr case=end

#
