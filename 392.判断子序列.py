#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#
# https://leetcode.cn/problems/is-subsequence/description/
#
# algorithms
# Easy (52.63%)
# Likes:    1080
# Dislikes: 0
# Total Accepted:    472.6K
# Total Submissions: 897.8K
# Testcase Example:  '"abc"\n"ahbgdc"'
#
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
#
#
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
#
# 进阶：
#
# 如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T
# 的子序列。在这种情况下，你会怎样改变代码？
#
# 致谢：
#
# 特别感谢 @pbrother 添加此问题并且创建所有测试用例。
#
#
#
# 示例 1：
#
#
# 输入：s = "abc", t = "ahbgdc"
# 输出：true
#
#
# 示例 2：
#
#
# 输入：s = "axc", t = "ahbgdc"
# 输出：false
#
#
#
#
# 提示：
#
#
# 0
# 0
# 两个字符串都只由小写字符组成。
#
#
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
# @lc code=end
def build_index(t):
    index = {}
    last_pos = {}  # 存储每个字符第一次出现的位置
    for i, char in enumerate(t):
        if char not in last_pos:
            last_pos[char] = i
        index[char] = last_pos[char]
    return index

def is_subsequence(s, t, index):
    pos = -1  # 起始位置
    for char in s:
        if char not in index or index[char] <= pos:
            return False
        pos = index[char]
    return True

def process_strings(strings, t):
    index = build_index(t)
    for s in strings:
        yield is_subsequence(s, t, index)

# 假设 strings 是一个巨大的字符串列表
# 为了演示，这里使用一个小列表
strings = ["abc", "def", "ghi", "jkl"]

# 使用生成器处理字符串
results = process_strings(strings, "aabcdefghij")
# for result in results:
#     print(result)
print(results)
