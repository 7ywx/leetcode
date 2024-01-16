#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# https://leetcode.cn/problems/group-anagrams/description/
#
# algorithms
# Medium (67.75%)
# Likes:    1792
# Dislikes: 0
# Total Accepted:    593.5K
# Total Submissions: 875.5K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
#
# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
#
#
#
# 示例 1:
#
#
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# 示例 2:
#
#
# 输入: strs = [""]
# 输出: [[""]]
#
#
# 示例 3:
#
#
# 输入: strs = ["a"]
# 输出: [["a"]]
#
#
#
# 提示：
#
#
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] 仅包含小写字母
#
#
#
from typing import Optional
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in hashtable:
                hashtable[key] = [s]
            else:
                hashtable[key].append(s)
        return list(hashtable.values())
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     anagrams = defaultdict(list) # 当试图访问 anagrams 中尚未存在的键时，它将自动创建并关联一个空列表作为该键的值。

    #     for s in strs:
    #         # 使用排序后的字符串作为 key，将字母异位词分到同一组
    #         key = ''.join(sorted(s))
    #         anagrams[key].append(s)

    #     return list(anagrams.values())
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     def is_anagram(s1, s2):
    #         if len(s1) != len(s2):
    #             return False
    #         char_count = {}
    #         for char in s1:
    #             char_count[char] = char_count.get(char, 0) + 1
    #         for char in s2:
    #             if char not in char_count or char_count[char] == 0:
    #                 return False
    #             char_count[char] -= 1
    #         return all(count == 0 for count in char_count.values())
    #     def is_anagram_wrong(s1, s2):
    #         if len(s1) != len(s2):
    #             return False
    #         char_count = {}
    #         for char in s1:
    #             char_count[char] = char_count.get(char, 0) + 1
    #         for char in s2:
    #             if char not in char_count or char_count[char] == 0:
    #                 return False
    #             char_count[char] -= 1
    #         # 错误地在这里直接返回True
    #         return True
    #     hashtable = {}
    #     sorted_strs = []
    #     result = []
    #     i = 0
    #     for index, s in enumerate(strs):
    #         sorted_strs.append("".join(sorted(s)))
    #     for index, s in enumerate(sorted_strs):
    #         if s not in hashtable:
    #             result.append([strs[index]])
    #             hashtable[s] = i
    #             i += 1
    #         else:
    #             result[hashtable[s]].append(strs[index])
    #     print(result)
    #     return result
# @lc code=end
solution = Solution()
solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
'''
# 可变类型的例子 - 列表作为字典键会引发错误
mutable_dict = {}  # 创建一个空字典
key = 1  # 定义一个变量作为键

# 尝试将变量作为字典的键添加元素
mutable_dict[key] = 'value'

# 改变变量的值
key = 2

print(mutable_dict[key])
'''
