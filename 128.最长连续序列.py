#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# https://leetcode.cn/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (52.87%)
# Likes:    1949
# Dislikes: 0
# Total Accepted:    521.4K
# Total Submissions: 988.5K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
#
#
# 示例 1：
#
#
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
#
# 示例 2：
#
#
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
#
#
#
#
# 提示：
#
#
# 0
# -10^9
#
#
#
from typing import Optional
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = defaultdict(list)
        set_nums = sorted(list(set(nums)))
        i = 0
        max_len = 0
        while i < len(set_nums):
            sums = 1
            while i < len(set_nums)-1 and set_nums[i]+1 == set_nums[i+1]:
                sums += 1
                i += 1
            if sums > max_len:
                max_len = sums
            i += 1
        return max_len
# @lc code=end
solution = Solution()
solution.longestConsecutive([100,4,200,1,3,2])
