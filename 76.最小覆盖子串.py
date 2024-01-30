#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode.cn/problems/minimum-window-substring/description/
#
# algorithms
# Hard (45.51%)
# Likes:    2810
# Dislikes: 0
# Total Accepted:    509.3K
# Total Submissions: 1.1M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 ""
# 。
#
#
#
# 注意：
#
#
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。
#
#
#
#
# 示例 1：
#
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
#
#
# 示例 2：
#
#
# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串 s 是最小覆盖子串。
#
#
# 示例 3:
#
#
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。
#
#
#
# 提示：
#
#
# ^m == s.length
# ^n == t.length
# 1 <= m, n <= 10^5
# s 和 t 由英文字母组成
#
#
#
# 进阶：你能设计一个在 o(m+n) 时间内解决此问题的算法吗？
#

# @lc code=start
from typing import Optional
from typing import List
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def judge(s_count, t_count) -> bool:
            for k in t_count.keys():
                if t_count[k] > s_count[k]:
                    return False
            return True
        left, right, s_len = 0, len(t)-1, len(s)
        min_left = 0
        min_right = 0
        min_len = s_len + 1
        s_count = Counter(s[left:right+1])
        t_count = Counter(t)
        while right < s_len:
            if judge(s_count, t_count):
                if min_len > right - left + 1:
                    min_len = right - left + 1
                    min_left = left
                    min_right = right
                s_count[s[left]] -= 1
                left += 1
            else:
                right += 1
                if right < s_len:
                    s_count[s[right]] += 1
        return s[min_left:min_right+1] if min_len <= s_len else "" # min_len < s_len + 1
# @lc code=end
s = Solution()
s.minWindow("ADOBECODEBANC", "ABC")
