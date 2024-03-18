#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode.cn/problems/generate-parentheses/description/
#
# algorithms
# Medium (77.57%)
# Likes:    3533
# Dislikes: 0
# Total Accepted:    807.7K
# Total Submissions: 1M
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
# 示例 1：
#
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#
#
# 示例 2：
#
#
# 输入：n = 1
# 输出：["()"]
#
#
#
#
# 提示：
#
#
# 1 <= n <= 8
#
#
#
from typing import List, Optional
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #TODO 没有get到
        def dfs(s, left, right, res):
            if left == 0 and right == 0:
                res.append(s)
                return
            if left > 0:
                dfs(s + '(', left - 1, right, res)
            if right > left:
                dfs(s + ')', left, right - 1, res)
        res = []
        dfs('', n, n, res)
        return res
# @lc code=end
solution = Solution()
print(solution.generateParenthesis(3))
