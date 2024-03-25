#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#
# https://leetcode.cn/problems/decode-string/description/
#
# algorithms
# Medium (57.37%)
# Likes:    1713
# Dislikes: 0
# Total Accepted:    301.1K
# Total Submissions: 524.8K
# Testcase Example:  '"3[a]2[bc]"'
#
# 给定一个经过编码的字符串，返回它解码后的字符串。
#
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
#
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
#
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
#
#
#
# 示例 1：
#
#
# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
#
#
# 示例 2：
#
#
# 输入：s = "3[a2[c]]"
# 输出："accaccacc"
#
#
# 示例 3：
#
#
# 输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
#
#
# 示例 4：
#
#
# 输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 30
# s 由小写英文字母、数字和方括号 '[]' 组成
# s 保证是一个 有效 的输入。
# s 中所有整数的取值范围为 [1, 300] 
#
#
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        """
        解码给定的字符串，恢复其原始加密形式。

        参数:
        s: str - 待解码的字符串，其中包含数字和字符，以及用方括号包围的数字和字符组合。

        返回:
        str - 解码后的字符串，恢复到原始的未加密状态。
        """
        stack = []  # 用于存储解码过程中的子字符串
        num = ""  # 用于存储当前括号内数字的临时变量

        for i in s:
            if i != "]":
                stack.append(i)  # 遇到非右括号字符，直接入栈
            else:
                temp = ""
                # 从栈顶开始，直到找到对应的左括号，将期间的字符逆序拼接
                while stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop()  # 弹出左括号“[”
                # 处理数字，逆序拼接并转换为整数
                while stack and stack[-1].isdigit(): #TODO .isdigit()
                    num = stack.pop() + num
                num = int(num)  # 将字符串数字转换为整数
                # 将之前拼接的字符根据数字重复次数入栈
                stack.append(temp * num)
                num = ""  # 重置数字变量

        return "".join(stack)  # 将栈中所有字符连接成最终的解码字符串
# @lc code=end
s = Solution()
# print(s.decodeString("3[a]2[bc]"))
# print(s.decodeString("3[a2[c]]"))
print(s.decodeString("10[a]"))
