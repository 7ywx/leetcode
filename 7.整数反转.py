#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode.cn/problems/reverse-integer/description/
#
# algorithms
# Medium (35.43%)
# Likes:    3950
# Dislikes: 0
# Total Accepted:    1.3M
# Total Submissions: 3.6M
# Testcase Example:  '123'
#
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
#
# 如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
#
#
#
# 示例 1：
#
#
# 输入：x = 123
# 输出：321
#
#
# 示例 2：
#
#
# 输入：x = -123
# 输出：-321
#
#
# 示例 3：
#
#
# 输入：x = 120
# 输出：21
#
#
# 示例 4：
#
#
# 输入：x = 0
# 输出：0
#
#
#
#
# 提示：
#
#
# -2^31
#
#
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        sign = 1 if x >= 0 else -1
        x = abs(x)
        res = 0
        while x > 0:
            digit = x % 10
            res = 10 * res +  digit
            if res > INT_MAX:
                return 0
            x //= 10
        return res * sign

        # digits = []  # 用于存储 x 的每一位数字
        # if x < 0:
        #     digits.append(-1)  # 如果 x 是负数，则将负号记录在 digits 中
        #     x = -x  # 将 x 转变为正数
        # while x != 0:
        #     digits.append(x % 10)  # 将 x 的个位数记录在 digits 中
        #     x //= 10  # x 去除个位数
        # digits = digits[::-1]  # 将 digits 反转
        # num = 0  # 用于存储反转后的数字
        # for i in range(len(digits)):
        #     if digits[i] == -1:  # 如果遇到负号，则将 num 取反
        #         num = -num
        #         break
        #     num += digits[i] * (10 ** i)  # 将每位数字与对应的位数相乘并累加到 num 上
        # if not (num < -2**31 or num > 2**31 - 1):  # 如果 num 的值在 int 的范围内
        #     return num  # 返回反转后的数字
        # else:
        #     return 0  # 如果 num 的值超出 int 的范围，则返回 0
# @lc code=end
solution = Solution()
solution.reverse(123)
solution.reverse(-123)
solution.reverse(120)
solution.reverse(0)
solution.reverse(1534236469)
