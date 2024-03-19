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
        if not digits:
            return []

        # 定义数字与字母的映射关系
        phone_mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index, path):
            # 如果当前组合长度与输入数字串长度相等，将其添加到结果集
            if index == len(digits):
                result.append(''.join(path))
                return

            # 获取当前数字对应的字母集合
            current_letters = phone_mapping[digits[index]]

            # 遍历当前数字对应的字母集合
            for letter in current_letters:
                path.append(letter)  # 添加当前字母到路径
                backtrack(index + 1, path)  # 递归处理下一个数字
                path.pop()  # 回溯，移除当前字母，尝试下一个字母

        result = []  # 存储最终结果的数组
        backtrack(0, [])  # 从第一个数字开始递归构建组合
        return result
# @lc code=end
solution = Solution()
print(solution.letterCombinations("23"))
