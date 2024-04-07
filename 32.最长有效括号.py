#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode.cn/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (37.80%)
# Likes:    2478
# Dislikes: 0
# Total Accepted:    438K
# Total Submissions: 1.2M
# Testcase Example:  '"(()"'
#
# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
#
#
#
#
#
# 示例 1：
#
#
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
#
#
# 示例 2：
#
#
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
#
#
# 示例 3：
#
#
# 输入：s = ""
# 输出：0
#
#
#
#
# 提示：
#
#
# 0 <= s.length <= 3 * 10^4
# s[i] 为 '(' 或 ')'
#
#
#
#
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 初始化栈和有效性数组
        stack = []
        isValid = [False] * (len(s)) # 记录每个位置是否是合法的括号

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    last = stack.pop()
                    # 标记对应 ( 括号和当前 ) 括号位置为有效
                    isValid[i] = True
                    isValid[last] = True
                # else:
                #     stack.append((i, s[i])) # 如果栈为空，说明没有匹配的开括号，将当前字符及其位置入栈

        # 计算最大连续有效括号长度
        ans, t = 0, 0
        for i in range(len(isValid)):
            if isValid[i]:
                t += 1
                if t > ans:
                    ans = t
            else:
                t = 0
        return ans

# @lc code=end
s = Solution()
print(s.longestValidParentheses("(()"))
print(s.longestValidParentheses(")()())"))
