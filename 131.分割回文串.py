#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# https://leetcode.cn/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (73.47%)
# Likes:    1751
# Dislikes: 0
# Total Accepted:    377.9K
# Total Submissions: 514.3K
# Testcase Example:  '"aab"'
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
#
#
#
# 示例 1：
#
#
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
#
#
# 示例 2：
#
#
# 输入：s = "a"
# 输出：[["a"]]
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 16
# s 仅由小写英文字母组成
#
#
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
# @lc code=end
