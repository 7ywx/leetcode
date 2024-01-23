#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#
# https://leetcode.cn/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (44.39%)
# Likes:    2225
# Dislikes: 0
# Total Accepted:    394K
# Total Submissions: 887.5K
# Testcase Example:  '[1,1,1]\n2'
#
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
#
# 子数组是数组中元素的连续非空序列。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,1,1], k = 2
# 输出：2
#
#
# 示例 2：
#
#
# 输入：nums = [1,2,3], k = 3
# 输出：2
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
#
#
#
from typing import Optional
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums_length = len(nums)
        res = 0
        prefix_sum = 0
        prefix_sum_count = Counter([0])
        for i in range(nums_length):
            prefix_sum += nums[i]
            if prefix_sum - k in prefix_sum_count:
                res += prefix_sum_count[prefix_sum - k]
            prefix_sum_count[prefix_sum] += 1
        print(prefix_sum_count)
        return res
        # prefix_sum = [0] * (nums_length + 1) # 前缀和: prefix_sum[i] = nums前i个元素的和, prefix_sum[0] = 0
        # prefix_sum_count = {0:1} # 前缀和出现次数
        # res = 0
        # for i in range(nums_length):
        #     prefix_sum[i+1] = prefix_sum[i] + nums[i]
        #     count
        #     if prefix_sum[i+1] - k in prefix_sum_count:
        #         res += prefix_sum_count[prefix_sum[i+1] - k]
        # # # 暴力破解
        # # for i in range(len(nums)):
        # #     for j in range(i, len(nums)):
        # #         if hashtable[j+1] - hashtable[i] == k:
        # #             res += 1
        # # # print(res)
        return res
# @lc code=end
solution = Solution()
solution.subarraySum(nums = [1,2,3], k = 3)
