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
        t = Counter(t)
        s_len = len(s)
        left, right, window, min_len = 0, 0, Counter(), s_len + 1
        min_left, min_right = 0, s_len
        less = len(t) # window（滑动窗口）有 less 种字母的出现次数 < t 中的字母出现次数
        while right < s_len:
            window[s[right]] += 1
            if window[s[right]] == t[s[right]]:
                less -= 1

            while less == 0: # window >= t
                if right - left + 1 < min_len:
                    min_left = left
                    min_right = right
                    min_len = right - left + 1

                if window[s[left]] == t[s[left]]:
                    less += 1
                window[s[left]] -= 1
                left += 1

            right += 1

        return s[min_left:min_right+1] if min_len < s_len + 1 else ""

# @lc code=end
s = Solution()
print(s.minWindow("a", "a"))
# 最长模版
'''
# 初始化指针和结果
left, right, result, bestResult = 0, 0, 0, 0

# 循环直到右指针到达结尾
while (右指针没有到结尾):
    # 窗口扩大，加入right对应元素，更新当前result
    result += 加入元素(right)

    # 检查当前result是否不满足要求
    while (result不满足要求):
        # 窗口缩小，移除left对应元素，left右移
        result -= 移除元素(left)
        left += 1

    # 如果当前result更优，更新最佳结果
    bestResult = max(bestResult, result)

    # 右指针右移
    right += 1

# 返回最佳结果
return bestResult
'''

# 最短模版
'''
# 初始化指针和结果
left, right, result, bestResult = 0, 0, inf, inf

# 循环直到右指针到达结尾
while (右指针没有到结尾):
    # 窗口扩大，加入right对应元素，更新当前result
    result += 加入元素(right)

    # 检查当前result是否满足要求
    while (result满足要求):
        # 如果当前result更优，更新最佳结果
        bestResult = min(bestResult, result)

        # 窗口缩小，移除left对应元素，left右移
        result -= 移除元素(left)
        left += 1

    # 右指针右移
    right += 1

# 返回最佳结果
return bestResult
'''
