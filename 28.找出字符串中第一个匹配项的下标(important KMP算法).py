#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#
# https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
#
# algorithms
# Easy (44.03%)
# Likes:    2272
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 2.6M
# Testcase Example:  '"sadbutsad"\n"sad"'
#
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0
# 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。
#
#
#
# 示例 1：
#
#
# 输入：haystack = "sadbutsad", needle = "sad"
# 输出：0
# 解释："sad" 在下标 0 和 6 处匹配。
# 第一个匹配项的下标是 0 ，所以返回 0 。
#
#
# 示例 2：
#
#
# 输入：haystack = "leetcode", needle = "leeto"
# 输出：-1
# 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
#
#
#
#
# 提示：
#
#
# 1 <= haystack.length, needle.length <= 10^4
# haystack 和 needle 仅由小写英文字符组成
#
#
#

from typing import List
# @lc code=start
class Solution:
    def buildNext(self, s: str) -> List[int]:
        #标签 next数组 KMP算法
        next = [0]
        prefix_len = 0 # 当前共同前后缀长度
        i = 1
        # ABACABAB
        while i < len(s):
            if s[i] == s[prefix_len]:
                prefix_len += 1
                next.append(prefix_len)
                i += 1
            else:
                if prefix_len == 0:
                    next.append(0)
                    i += 1
                else:
                    prefix_len = next[prefix_len - 1]
            # print(f"next_{i} = {next}")
        return next
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        next = self.buildNext(needle)
        i = 0 # haystack的指针
        j = 0 # needle的指针
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j # 匹配成功，返回主串匹配的下标
            else:
                if j == 0:
                    i += 1
                else:
                    j = next[j - 1]
        return -1

        # return haystack.find(needle)
# @lc code=end
s = Solution()
haystack = "sadbutsad"
needle = "abacabab"
print(s.strStr(haystack, needle))
