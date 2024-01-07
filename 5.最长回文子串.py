#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode.cn/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (37.92%)
# Likes:    7012
# Dislikes: 0
# Total Accepted:    1.6M
# Total Submissions: 4.2M
# Testcase Example:  '"babad"'
#
# 给你一个字符串 s，找到 s 中最长的回文子串。
#
# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
#
#
#
# 示例 1：
#
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#
#
# 示例 2：
#
#
# 输入：s = "cbbd"
# 输出："bb"
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成
#
#
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(s):
            return s == s[::-1]
        result = set()
        for i in range(len(s)+1):
            for j in range(i+1, len(s)+1):
                result.add(s[i:j])

# @lc code=end
