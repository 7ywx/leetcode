#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from typing import Optional
from typing import List
import collections
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # v1.1 defaultdict版本
        # hashtable = collections.defaultdict()
        # for index, num in enumerate(nums):
        #     if target - num in hashtable:
        #         return [index, hashtable[target - num]]
        #     hashtable[num] = index
        # return False

        # v1 哈希表
        hashtable = {}
        for index, num in enumerate(nums):
            if target - num in hashtable: # 在 if a in hashtable: 这样的条件判断中，Python会检查字典（哈希表）hashtable 的键（keys）中是否包含变量 a。也就是说，它不会查找值（values），而是查找键。
                return [hashtable[target - num], index] # 如果存在，返回对应的下标。
            hashtable[num] = index # 将当前元素及其下标存入哈希表
        return [] # 如果不存在，返回空列表。
# @lc code=end
solution = Solution()
print(solution.twoSum(nums=[2, 7, 11, 15], target=9))
