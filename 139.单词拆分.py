#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
# https://leetcode.cn/problems/word-break/description/
#
# algorithms
# Medium (55.22%)
# Likes:    2456
# Dislikes: 0
# Total Accepted:    559.3K
# Total Submissions: 1M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。
#
# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
#
#
#
# 示例 1：
#
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
#
#
# 示例 2：
#
#
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
# 注意，你可以重复使用字典中的单词。
#
#
# 示例 3：
#
#
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s 和 wordDict[i] 仅由小写英文字母组成
# wordDict 中的所有字符串 互不相同
#
#
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        判断一个字符串是否可以由字典中的单词组成。

        参数:
        s: 待判断的字符串。
        wordDict: 字典，包含可能的单词。

        返回值:
        布尔值，如果s可以由字典中的单词组成，则返回True；否则返回False。
        """
        dp = [False] * (len(s) + 1) # 初始化动态规划数组，dp[i]表示s[0:i]是否可以由wordDict中的单词组成
        dp[0] = True # 空字符串可以由字典中的单词组成
        for i in range(1, len(s) + 1):
            # 遍历字符串s的每个子串
            for j in range(i):
                # 尝试从s的开头到当前位置的子串
                if dp[j] and s[j:i] in wordDict:
                    # 如果之前的子串可以由字典组成，并且当前子串也在字典中
                    dp[i] = True # 则标记为可以由字典组成
                    break
        return dp[-1] # 返回最后一个元素，表示整个字符串s是否可以由字典组成
# @lc code=end
