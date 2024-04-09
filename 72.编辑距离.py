#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
# https://leetcode.cn/problems/edit-distance/description/
#
# algorithms
# Medium (62.81%)
# Likes:    3354
# Dislikes: 0
# Total Accepted:    467.7K
# Total Submissions: 744.4K
# Testcase Example:  '"horse"\n"ros"'
#
# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
#
# 你可以对一个单词进行如下三种操作：
#
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
#
#
#
#
# 示例 1：
#
#
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#
#
# 示例 2：
#
#
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#
#
#
#
# 提示：
#
#
# 0 <= word1.length, word2.length <= 500
# word1 和 word2 由小写英文字母组成
#
#
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j]: 从word1的前i个字符转换到word2的前j个字符所需的最少操作数。
        dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        for j in range(len(word1) + 1):
            dp[0][j] = j
        for i in range(len(word2) + 1):
            dp[i][0] = i
        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word2[i-1] == word1[j-1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 从dp[i-1][j]（删除）、dp[i][j-1]（插入）、dp[i-1][j-1]（替换）
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]
# @lc code=end
