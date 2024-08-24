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
    def getNext(self, next: List[int], s: str) -> None:
        #标签 next数组 KMP算法
        prefix_len = 0
        i = 1
        while i < len(s):
            if s[i] == s[prefix_len]:
                prefix_len += 1
                next[i] = prefix_len
                i += 1
            else:
                if prefix_len == 0:
                    next[i] = 0
                    i += 1
                else:
                    prefix_len = next[prefix_len - 1]
            # print(f"next_{i} = {next}")
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        next = [0] * len(needle)
        self.getNext(next, needle)
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1

        # return haystack.find(needle)
# @lc code=end
s = Solution()
haystack = "sadbutsad"
needle = "abacabab"
print(s.strStr(haystack, needle))
