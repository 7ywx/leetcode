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
from typing import List, Optional
# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #TODO 搞懂
        dp = [[[]]]
        # dp[i]表示s[:i]所有可能的分割方案
        for i in range(1, len(s) + 1):
            dp.append([])
            for j in range(i):
                tmp = s[j:i]
                if tmp == tmp[::-1]:
                    dp[-1].extend(l + [tmp] for l in dp[j])
        return dp[-1]

        # 回溯
        path = []
        res = []
        s_len = len(s)
        def isPalindrome(s: str)->bool:
            return s == s[::-1]
        def dfs(startIndex): # startIndex: [0, ]
            if startIndex == s_len:
                res.append(path[:])
                return
            for i in range(startIndex, s_len): # 分割线画在startIndex元素的后面
                if isPalindrome(s[startIndex:i+1]):
                    path.append(s[startIndex:i+1])
                    dfs(i+1)
                    path.pop()
        dfs(0)
        return res
# @lc code=end
s = Solution()
print(s.partition("aab"))
