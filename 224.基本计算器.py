#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#
# https://leetcode.cn/problems/basic-calculator/description/
#
# algorithms
# Hard (42.96%)
# Likes:    1069
# Dislikes: 0
# Total Accepted:    156.1K
# Total Submissions: 363.4K
# Testcase Example:  '"1 + 1"'
#
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
#
# 注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。
#
#
#
# 示例 1：
#
#
# 输入：s = "1 + 1"
# 输出：2
#
#
# 示例 2：
#
#
# 输入：s = " 2-1 + 2 "
# 输出：3
#
#
# 示例 3：
#
#
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 3 * 10^5
# s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
# s 表示一个有效的表达式
# '+' 不能用作一元运算(例如， "+1" 和 "+(2 + 3)" 无效)
# '-' 可以用作一元运算(即 "-1" 和 "-(2 + 3)" 是有效的)
# 输入中不存在两个连续的操作符
# 每个数字和运行的计算将适合于一个有符号的 32位 整数
#
#
#
from collections import deque
# @lc code=start

class Solution:
    def calculate(self, s: str) -> int:
        # 存放所有的数字
        nums = []
        # 为了防止第一个数为负数，先往 nums 加个 0
        nums.append(0)
        # 将所有的空格去掉
        s = s.replace(" ", "")
        # 存放所有的操作符，包括 +/-
        ops = []
        n = len(s)
        i = 0
        while i < n:
            c = s[i]
            if c == '(':
                ops.append(c)
            elif c == ')':
                # 计算到最近一个左括号为止
                while ops and ops[-1] != '(':
                    self.calc(nums, ops)
                # 移除左括号
                ops.pop()
            else:
                if c.isdigit():
                    u = 0
                    j = i
                    # 将从 i 位置开始后面的连续数字整体取出，加入 nums
                    while j < n and s[j].isdigit():
                        u = u * 10 + int(s[j])
                        j += 1
                    nums.append(u)
                    i = j - 1
                else: # 运算符
                    if i > 0 and (s[i - 1] in '('): # 为了防止第一个数为负数，先往 nums 加个 0
                        nums.append(0)
                    # 有一个新操作符要入栈时，先把栈内可以算的都算了
                    while ops and ops[-1] != '(':
                        self.calc(nums, ops)
                    ops.append(c)
            i += 1
        # 计算剩余的操作
        while ops:
            self.calc(nums, ops)

        return nums[-1]

    def calc(self, nums: deque, ops: deque):
        if len(nums) < 2 or not ops:
            return
        b = nums.pop()
        a = nums.pop()
        op = ops.pop()
        result = a + b if op == '+' else a - b
        nums.append(result)
# @lc code=end
print(Solution().calculate("1-(     -2)"))
