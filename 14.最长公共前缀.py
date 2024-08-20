#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode.cn/problems/longest-common-prefix/description/
#
# algorithms
# Easy (43.97%)
# Likes:    3124
# Dislikes: 0
# Total Accepted:    1.3M
# Total Submissions: 3M
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
#
#
# 示例 1：
#
#
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
#
#
# 示例 2：
#
#
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
#
#
#
# 提示：
#
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成
#
#
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        查找字符串列表中最长的公共前缀。

        参数:
        strs: List[str]，一个包含多个字符串的列表。

        返回值:
        str，找到的最长公共前缀字符串。
        """
        ans = ""  # 初始化存储最长公共前缀的字符串

        # 遍历第一个字符串的每个字符
        for i in range(len(strs[0])):
            # 对于后续每个字符串，检查当前字符是否与第一个字符串的对应字符相同
            for j in range(1, len(strs)):
                # 如果已经超出当前字符串的长度或者当前字符不匹配，则返回当前的最长公共前缀
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return ans
            # 如果所有字符串的当前字符都匹配，则将该字符添加到最长公共前缀中
            ans += strs[0][i]
        return ans
# @lc code=end
