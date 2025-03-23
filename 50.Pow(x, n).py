from typing import List
#
# @lc app=leetcode.cn id=50 lang=python3
# @lcpr version=20001
#
# [50] Pow(x, n)
#
# https://leetcode.cn/problems/powx-n/description/
#
# algorithms
# Medium (38.59%)
# Likes:    1395
# Dislikes: 0
# Total Accepted:    483.9K
# Total Submissions: 1.3M
# Testcase Example:  '2.00000\n10'
#
# 实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，x^n^ ）。
#
#
#
# 示例 1：
#
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
#
#
# 示例 2：
#
# 输入：x = 2.10000, n = 3
# 输出：9.26100
#
#
# 示例 3：
#
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2^-2 = 1/2^2 = 1/4 = 0.25
#
#
#
#
# 提示：
#
#
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# n 是一个整数
# 要么 x 不为零，要么 n > 0 。
# -10^4 <= x^n <= 10^4
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n < 0:  # x^-n = (1/x)^n
            n = -n
            x = 1 / x
        while n:  # 从低到高枚举 n 的每个比特位
            if n & 1:  # 这个比特位是 1
                ans *= x  # 把 x 乘到 ans 中
            x *= x  # x 自身平方
            n >>= 1  # 继续枚举下一个比特位
        return ans

        def quick_pow(x, n):
            if n == 0:
                return 1
            if n % 2 == 0:
                return quick_pow(x * x, n // 2)
            else:
                return x * quick_pow(x * x, n // 2)

        if n < 0:
            x = 1 / x
            n = -n

        return quick_pow(x, n)

        # O(n) 超时
        if n == 0:
            return 1
        elif n > 0:
            ans = 1
            for i in range(0, n):
                ans *= x
            return ans
        else:
            ans = 1
            n = -n
            for i in range(0, n):
                ans /= x
            return ans
# @lc code=end



#
# @lcpr case=start
# 2.00000\n10\n
# @lcpr case=end

# @lcpr case=start
# 2.10000\n3\n
# @lcpr case=end

# @lcpr case=start
# 2.00000\n-2\n
# @lcpr case=end

#
