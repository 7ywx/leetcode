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
        prefix_sum_count = {0:1} # {前缀和:出现次数}
        prefix_sum = 0 # 包括当前位置的前缀和
        res = 0
        for n in nums:
            prefix_sum += n # prefix_sum意为从当前元素到开始位置的子数组
            res += prefix_sum_count.get(prefix_sum-k,0) # prefix_sum - (prefix_sum - k) = k 通过前缀和来确定一个子数组
            prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum,0) + 1
        return res

        # res = 0
        # prefix_sum = 0
        # prefix_sum_count = Counter([0])
        # for n in nums:
        #     prefix_sum += n
        #     if prefix_sum - k in prefix_sum_count:
        #         res += prefix_sum_count[prefix_sum - k]
        #     prefix_sum_count[prefix_sum] += 1
        # return res

        # # # 暴力破解
        # # for i in range(len(nums)):
        # #     for j in range(i, len(nums)):
        # #         if hashtable[j+1] - hashtable[i] == k:
        # #             res += 1
        # # # print(res)
# @lc code=end
solution = Solution()
solution.subarraySum(nums = [1,2,3], k = 3)
