#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (54.02%)
# Likes:    1365
# Dislikes: 0
# Total Accepted:    365.5K
# Total Submissions: 676.7K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
#
#
#
# 示例 1:
#
#
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
#
#
# 示例 2:
#
#
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
#
#
#
#
# 提示:
#
#
# 1 <= s.length, p.length <= 3 * 10^4
# s 和 p 仅包含小写字母
#
#
#
from typing import Optional
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
        result = []
        len_p, len_s = len(p), len(s)

        if len_s < len_p:
            return result

        # 计算目标字母异位词的数组计数 and 初始化滑动窗口的数组计数
        p_count = [0] * 26
        window_count = [0] * 26
        for i in range(len_p):
            p_count[ord(p[i]) - ord('a')] += 1
            window_count[ord(s[i]) - ord('a')] += 1

        # 滑动窗口比较
        for i in range(len_s - len_p + 1): # i: 滑动窗口的起始位置
            if window_count == p_count:
                result.append(i)

            # 移动滑动窗口
            if i + len_p < len_s: # if下一个滑动窗口的结束位置 < s的长度 则可以滑动一格
                window_count[ord(s[i]) - ord('a')] -= 1
                window_count[ord(s[i + len_p]) - ord('a')] += 1

        return result

        # result = []
        # len_p, len_s = len(p), len(s)

        # if len_s < len_p:
        #     return result

        # # 计算字母异位词的哈希表
        # p_count = Counter(p)

        # # 初始化滑动窗口的哈希表
        # window_count = Counter(s[:len_p])

        # for i in range(len_s - len_p + 1):
        #     # 检查当前窗口是否是字母异位词
        #     if window_count == p_count:
        #         result.append(i)

        #     # 移动滑动窗口
        #     if i + len_p < len_s:
        #         window_count[s[i]] -= 1
        #         if window_count[s[i]] == 0:
        #             del window_count[s[i]]
        #         window_count[s[i + len_p]] += 1

        # return result

        # # 初始化相关变量
        # n, m, res = len(s), len(p), []
        # # 特解
        # if n < m: return res
        # # 初始化两个长度为 26 的数组
        # p_cnt = [0] * 26
        # s_cnt = [0] * 26
        # # 遍历p并根据每个字母的ASCII码值，将出现次数记录到数组p_cnt中
        # for i in range(m):
        #     p_cnt[ord(p[i]) - ord('a')] += 1
        #     s_cnt[ord(s[i]) - ord('a')] += 1
        # if s_cnt == p_cnt:
        #     res.append(0)

        # # 遍历字符串p，并根据每个字母的ASCII码值，将出现次数记录到数组p_cnt中
        # for i in range(m,n):
        #     s_cnt[ord(s[i - m]) - ord('a')] -= 1 #移动末尾
        #     s_cnt[ord(s[i]) - ord('a')] += 1 #增大前端
        #     # 如果窗口截取的内容与p相等，那么增加答案计数
        #     if s_cnt == p_cnt:
        #         res.append(i - m + 1)

        # return res

        # left, right, res, pl, sl = 0, 0, [], len(p), len(s)
        # if sl < pl:
        #     return res
        # p_sorted = sorted(p)
        # while right < sl:
        #     right = left + pl
        #     if sorted(s[left:right]) == p_sorted:
        #         res.append(left)
        #     left += pl
        # # print(res)
        # return res
# @lc code=end
solution = Solution()
solution.findAnagrams(s = "cbaebabacd", p = "abc")
solution.findAnagrams(s = "abab", p = "ab")
