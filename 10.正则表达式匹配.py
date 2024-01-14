#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
# https://leetcode.cn/problems/regular-expression-matching/description/
#
# algorithms
# Hard (30.72%)
# Likes:    3821
# Dislikes: 0
# Total Accepted:    402.4K
# Total Submissions: 1.3M
# Testcase Example:  '"aa"\n"a"'
#
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
#
#
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
#
# 示例 1：
#
#
# 输入：s = "aa", p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
#
#
# 示例 2:
#
#
# 输入：s = "aa", p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#
#
# 示例 3：
#
#
# 输入：s = "ab", p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s 只包含从 a-z 的小写字母。
# p 只包含从 a-z 的小写字母，以及字符 . 和 *。
# 保证每次出现字符 * 时，前面都匹配到有效的字符
#
#
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # # 初始化一维数组，dp[j] 表示 s 的前 i 个字符是否与 p 的前 j 个字符匹配
        # dp = [False] * (len(p) + 1)
        # dp[0] = True

        # # 处理模式中可能存在连续 * 的情况
        # for j in range(1, len(p) + 1):
        #     if p[j - 1] == '*' and dp[j - 2]:
        #         dp[j] = True

        # # 动态规划递推
        # for i in range(1, len(s) + 1):
        #     prev, dp[0] = dp[0], False
        #     for j in range(1, len(p) + 1):
        #         tmp = dp[j]
        #         if p[j - 1] == s[i - 1] or p[j - 1] == '.':
        #             dp[j] = prev
        #         elif p[j - 1] == '*':
        #             dp[j] = dp[j - 2] or (dp[j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
        #         else:
        #             dp[j] = False
        #         prev = tmp

        # return dp[len(p)]



        # 构建二维动态规划数组，dp[i][j] 表示 s 的前 i 个字符是否与 p 的前 j 个字符匹配
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # 空字符串与空模式匹配
        dp[0][0] = True

        # 处理模式中可能存在连续 * 的情况
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*' and dp[0][j - 2]:
                dp[0][j] = True

        # 动态规划递推
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

        return dp[len(s)][len(p)]


        # i, j = 0, 0
        # while i < len(s) and j < len(p):
        #     if s[i] == p[j] or p[j] == '.' and p[j+1] != '*':
        #         i += 1
        #         j += 1
        #     elif p[j] == '*':
        #         if p[j - 1] == s[i] or p[j - 1] == '.':
        #             i += 1
        #             j += 1
        #         elif p[j - 1] != s[i] and p[j - 1] != '.': # 匹配0个，j往后
        #             j += 1
        #     else:
        #         if p[j+1] == '*':
        #             j += 2
        #             continue
        #         return False
        # if i == len(s) and j == len(p):
        #     return True
        # elif i < len(s) and j == len(p):
        #     return False
        # elif i == len(s) and j < len(p):
        #     while j < len(p) and p[j] == '*':
        #         j += 1
        #     return j == len(p)
# @lc code=end
solution = Solution()
print(solution.isMatch(s = "aaa", p = "ab*a*c*a"))
