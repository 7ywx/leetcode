#
# @lc app=leetcode.cn id=1047 lang=python3
# @lcpr version=30104
#
# [1047] 删除字符串中的所有相邻重复项
#
# https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/description/
#
# algorithms
# Easy (73.37%)
# Likes:    687
# Dislikes: 0
# Total Accepted:    370.8K
# Total Submissions: 505.1K
# Testcase Example:  '"abbaca"'
#
# 给出由小写字母组成的字符串 s，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
#
# 在 s 上反复执行重复项删除操作，直到无法继续删除。
#
# 在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
#
#
#
# 示例：
#
# 输入："abbaca"
# 输出："ca"
# 解释：
# 例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串
# "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 10^5
# s 仅由小写英文字母组成。
#
#
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        # 初始化一个空栈，用于临时存储字符
        stack = []

        # 遍历输入字符串中的每个字符
        for c in s:
            # 检查栈是否非空且栈顶字符与当前字符相同
            if stack and stack[-1] == c:
                # 如果相同，则移除栈顶字符，因为找到了一对相同的字符
                stack.pop()
            else:
                # 如果不相同或栈为空，则将当前字符压入栈中
                stack.append(c)
        # 最后，将栈中剩余的字符连接成字符串并返回。栈中剩余的字符都是没有找到配对的字符
        return "".join(stack)
# @lc code=end



#
# @lcpr case=start
# "abbaca"\n
# @lcpr case=end

#
