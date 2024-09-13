#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#
# https://leetcode.cn/problems/happy-number/description/
#
# algorithms
# Easy (64.93%)
# Likes:    1604
# Dislikes: 0
# Total Accepted:    560.9K
# Total Submissions: 863.8K
# Testcase Example:  '19'
#
# 编写一个算法来判断一个数 n 是不是快乐数。
#
# 「快乐数」 定义为：
#
#
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果这个过程 结果为 1，那么这个数就是快乐数。
#
#
# 如果 n 是 快乐数 就返回 true ；不是，则返回 false 。
#
#
#
# 示例 1：
#
#
# 输入：n = 19
# 输出：true
# 解释：
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
#
# 示例 2：
#
#
# 输入：n = 2
# 输出：false
#
#
#
#
# 提示：
#
#
# 1 <= n <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        # 快慢指针
        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1

        # 哈希
        seen = set()
        while n not in seen:
            seen.add(n)
            n = get_next(n) # n = sum(int(i)**2 for i in str(n))

        return n == 1

# @lc code=end
