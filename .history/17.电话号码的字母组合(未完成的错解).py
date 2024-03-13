#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (58.96%)
# Likes:    2777
# Dislikes: 0
# Total Accepted:    831.7K
# Total Submissions: 1.4M
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
#
#
# 示例 1：
#
#
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#
# 示例 2：
#
#
# 输入：digits = ""
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：digits = "2"
# 输出：["a","b","c"]
#
#
#
#
# 提示：
#
#
# 0 <= digits.length <= 4
# digits[i] 是范围 ['2', '9'] 的一个数字。
#
#
#
from typing import List, Optional
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_len = len(digits)
        if digits_len == 0:
            return []

        num_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        digits_num = [num_map[digit] for digit in digits]

        def backtrack(depth, path, used):
            # 将当前路径添加到结果集中
            if depth == digits_len:
                result.append(''.join(path[:]))
                return

            # 递归处理下一个元素
            for i in range(digits_len):
                if not used[i]:
                    used[i] = True
                    for j in range(len(digits_num[i])):
                        path.append(digits_num[i][j])
                        backtrack(depth + 1, path, used)
                        path.pop()  # 回溯，移除当前元素
                    used[i] = False

        result = []
        backtrack(0, [], [False for _ in range(digits_len)])
        return result
# @lc code=end
solution = Solution()
print(solution.letterCombinations("23"))
