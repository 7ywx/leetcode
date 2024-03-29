#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (39.37%)
# Likes:    9893
# Dislikes: 0
# Total Accepted:    2.6M
# Total Submissions: 6.7M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
#
#
#
# 示例 1:
#
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
# 示例 2:
#
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
# 示例 3:
#
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
#
#
# 提示：
#
#
# 0 <= s.length <= 5 * 10^4
# s 由英文字母、数字、符号和空格组成
#
#
#
from collections import defaultdict
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 标签 滑动窗口
        left, right, max_len, lens = 0, 0, 0, len(s) # 初始化左右窗口，最大长度
        d = defaultdict(int) # 记录字符的出现次数
        while right < lens:
            while d[s[right]]: # 当前字符在哈希表中出现，需要移动左指针直至出现次数为0
                d[s[left]] -= 1 # 将left指向的字符的出现次数减1
                left += 1 # 移动左指针
            d[s[right]] += 1 # 将right指向的字符的出现次数加1
            if right-left+1 > max_len: # max_len = max(max_len, right-left+1)这个慢
                max_len = right-left+1
            if max_len > lens-left-1: # 早停机制 当前max_len >= left到最后的字符长度，说明已经找到最大max_len，退出循环
                break
            right += 1 # 移动右指针,尝试寻找更长的无重复字符子串
        return max_len

        # left = 0
        # max_len = 0
        # for i in range(len(s)):
        #     if s[i] in d and d[s[i]] >= left: #对于每个字符，我们首先判断它是否已经在哈希表中出现过，并且其最后一次出现的位置在left和当前位置之间
        #         left = d[s[i]] + 1
        #     d[s[i]] = i
        #     max_len = max(max_len, i - left + 1)
        # return max_len

        # dic, res, i = {}, 0, -1
        # for j in range(len(s)):
        #     if s[j] in dic:
        #         i = max(dic[s[j]], i) # 更新左指针 i
        #     dic[s[j]] = j # 哈希表记录
        #     res = max(res, j - i) # 更新结果
        # return res

        # # 初始化变量
        # start = 0  # 滑动窗口的起始位置
        # end = 0  # 滑动窗口的结束位置
        # max_length = 0  # 记录最长子串的长度
        # char_set = []  # 记录已经出现过的字
        # # 遍历字符串
        # while end < len(s):
        #     # 如果当前字符已经出现过，移动窗口的起始位置到上一次出现的该字符的下一个位置
        #     if s[end] in char_set:
        #         max_length = max(max_length, end - start)
        #         start += 1
        #         char_set = [s[start]]
        #         end = start + 1
        #     else:
        #         char_set.append(s[end])
        #         max_length = max(max_length, end - start + 1)
        #         end += 1
        # #print(max_length)
        # return max_length
# @lc code=end
s = "dvdf"
s0 = "pwwkew"
s1 = "abba"
sol = Solution()
print(sol.lengthOfLongestSubstring(s1))
