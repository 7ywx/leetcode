#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode.cn/problems/valid-parentheses/description/
#
# algorithms
# Easy (43.91%)
# Likes:    4396
# Dislikes: 0
# Total Accepted:    1.8M
# Total Submissions: 4M
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
#
#
#
#
# 示例 1：
#
#
# 输入：s = "()"
# 输出：true
#
#
# 示例 2：
#
#
# 输入：s = "()[]{}"
# 输出：true
#
#
# 示例 3：
#
#
# 输入：s = "(]"
# 输出：false
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 10^4
# s 仅由括号 '()[]{}' 组成
#
#
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        """
        检查给定的字符串是否包含合法的括号、大括号或中括号。合法的字符串中，每个打开的括号都必须有一个对应的关闭括号。

        参数:
        s: 字符串，包含括号、大括号或中括号的字符序列。

        返回值:
        布尔值，如果字符串中的括号组合合法，则返回True；否则返回False。
        """
        stack = []  # 用于存储打开的括号的栈
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)  # 遇到打开的括号，推入栈中
            else:
                if len(stack) == 0:
                    return False  # 如果此时栈为空，则没有对应的打开括号，返回False
                if i == ')' and stack[-1] == '(':
                    stack.pop()  # 如果当前字符为')'且栈顶为'('，则匹配成功，弹出栈顶元素
                elif i == '}' and stack[-1] == '{':
                    stack.pop()  # 如果当前字符为'}'且栈顶为'{'，则匹配成功，弹出栈顶元素
                elif i == ']' and stack[-1] == '[':
                    stack.pop()  # 如果当前字符为']'且栈顶为'['，则匹配成功，弹出栈顶元素
                else:
                    return False  # 其他情况为匹配失败，返回False
        return True if len(stack) == 0 else False  # 最后栈为空则表示所有括号都已合法匹配，返回True；否则返回False# @lc code=end
