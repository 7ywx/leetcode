from typing import List
#
# @lc app=leetcode.cn id=67 lang=python3
# @lcpr version=20001
#
# [67] 二进制求和
#
# https://leetcode.cn/problems/add-binary/description/
#
# algorithms
# Easy (53.46%)
# Likes:    1236
# Dislikes: 0
# Total Accepted:    425.6K
# Total Submissions: 796K
# Testcase Example:  '"11"\n"1"'
#
# 给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
#
#
#
# 示例 1：
#
# 输入:a = "11", b = "1"
# 输出："100"
#
# 示例 2：
#
# 输入：a = "1010", b = "1011"
# 输出："10101"
#
#
#
# 提示：
#
#
# 1 <= a.length, b.length <= 10^4
# a 和 b 仅由字符 '0' 或 '1' 组成
# 字符串如果不是 "0" ，就不含前导零
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        i, j = len(a)-1, len(b)-1
        c = 0
        while i > -1 or j > -1:
            s = 0
            if i > -1:
                s += int(a[i])
            if j > -1:
                s += int(b[j])
            s += c
            if s < 2:
                ans = str(s) + ans
                c = 0
            elif s == 2:
                ans = "0" + ans
                c = 1
            else:
                ans = "1" + ans
                c = 1
            i -= 1
            j -= 1
        if c != 0:
            if c < 2:
                ans = "1" + ans
                c = 0
            elif c == 2:
                ans = "0" + ans
                ans = "1" + ans
            else:
                ans = "1" + ans
                ans = "1" + ans
        return ans
# @lc code=end

Solution().addBinary("11", "1")

#
# @lcpr case=start
# "11"\n"1"\n
# @lcpr case=end

# @lcpr case=start
# "1010"\n"1011"\n
# @lcpr case=end

#
