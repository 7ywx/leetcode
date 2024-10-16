from typing import List
#
# @lc app=leetcode.cn id=172 lang=python3
# @lcpr version=20001
#
# [172] 阶乘后的零
#
# https://leetcode.cn/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Medium (50.60%)
# Likes:    854
# Dislikes: 0
# Total Accepted:    212.3K
# Total Submissions: 419.7K
# Testcase Example:  '3'
#
# 给定一个整数 n ，返回 n! 结果中尾随零的数量。
#
# 提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
#
#
#
# 示例 1：
#
# 输入：n = 3
# 输出：0
# 解释：3! = 6 ，不含尾随 0
#
#
# 示例 2：
#
# 输入：n = 5
# 输出：1
# 解释：5! = 120 ，有一个尾随 0
#
#
# 示例 3：
#
# 输入：n = 0
# 输出：0
#
#
#
#
# 提示：
#
#
# 0 <= n <= 10^4
#
#
#
#
# 进阶：你可以设计并实现对数时间复杂度的算法来解决此问题吗？
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans


        '''
        n! 尾零的数量即为 n! 中因子 10 的个数，而 10=2×5，因此转换成求 n! 中质因子 2 的个数和质因子 5 的个数的较小值。

        由于质因子 5 的个数不会大于质因子 2 的个数（具体证明见方法二），我们可以仅考虑质因子 5 的个数。

        而 n! 中质因子 5 的个数等于 [1,n] 的每个数的质因子 5 的个数之和，我们可以通过遍历 [1,n] 的所有 5 的倍数求出。

        '''
        ans = 0
        for i in range(5, n + 1, 5):
            while i % 5 == 0:
                i //= 5
                ans += 1
        return ans


        # 暴力 超时
        if n == 0: return 0
        s = 1
        for i in range(1, n+1):
            s *= i
        ans = 0
        while s % 10 == 0:
            ans += 1
            s = s // 10
        return ans
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

#
