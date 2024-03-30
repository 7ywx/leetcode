#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#
# https://leetcode.cn/problems/partition-labels/description/
#
# algorithms
# Medium (76.85%)
# Likes:    1117
# Dislikes: 0
# Total Accepted:    221K
# Total Submissions: 287.6K
# Testcase Example:  '"ababcbacadefegdehijhklij"'
#
# 给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
#
# 注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
#
# 返回一个表示每个字符串片段的长度的列表。
#
#
# 示例 1：
#
#
# 输入：s = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。
#
# 示例 2：
#
#
# 输入：s = "eccbbbbdec"
# 输出：[10]
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 500
# s 仅由小写英文字母组成
#
#
#
from typing import List
# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        分割字符串中的连续子串，使得每个子串中的字符都只出现一次。

        参数:
        s: 字符串，需要进行分割的原始字符串。

        返回值:
        List[int]: 包含每个分割后子串长度的列表。
        """
        # 创建一个字典，用于存储每个字符在字符串中最后一次出现的索引
        last = {}
        # 获取字符串中不同字符的数量
        n = len(set(s))
        # 从字符串末尾向前遍历，记录每个字符的最后一次出现位置
        for c in range(len(s)-1, -1, -1):
            if s[c] not in last:
                last[s[c]] = c
            if len(last) == n:
                break
        # 初始化起始和结束索引
        start, end = 0, last[s[0]]
        res = []
        # 遍历字符串，根据结束索引将字符串分割成子串，并记录子串长度
        for i in range(len(s)):
            if i == end:
                res.append(end-start+1)
                start = i + 1
                if i != len(s)-1:
                    end = last[s[i+1]]
            else:
                # 更新结束索引为当前字符的最远出现位置
                if last[s[i]] > end: # end = max(end, last[s[i]])
                    end = last[s[i]]
        return res
# @lc code=end
s = Solution()
print(s.partitionLabels("eaaaabaaec"))
# print(s.partitionLabels("ababcbacadefegdehijhklij"))
