#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
# https://leetcode.cn/problems/valid-anagram/description/
#
# algorithms
# Easy (66.92%)
# Likes:    948
# Dislikes: 0
# Total Accepted:    840K
# Total Submissions: 1.3M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 字母异位词。
#
#
#
# 示例 1:
#
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#
#
# 示例 2:
#
#
# 输入: s = "rat", t = "car"
# 输出: false
#
#
#
# 提示:
#
#
# 1 <= s.length, t.length <= 5 * 10^4
# s 和 t 仅包含小写字母
#
#
#
#
# 进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
#
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        return sorted(s) == sorted(t)
# @lc code=end
