#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
# https://leetcode.cn/problems/majority-element/description/
#
# algorithms
# Easy (66.33%)
# Likes:    2167
# Dislikes: 0
# Total Accepted:    899.6K
# Total Submissions: 1.4M
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
# 示例 1：
#
#
# 输入：nums = [3,2,3]
# 输出：3
#
# 示例 2：
#
#
# 输入：nums = [2,2,1,1,1,2,2]
# 输出：2
#
#
#
# 提示：
#
#
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
#
#
#
#
# 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
#
#
from collections import defaultdict
from typing import List, Optional
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 分治法
        def majority_element_rec(lo, hi):
            if lo == hi:
                return nums[lo]

            mid = (hi - lo) // 2 + lo
            left_majority = majority_element_rec(lo, mid)
            right_majority = majority_element_rec(mid + 1, hi)

            if left_majority == right_majority:
                return left_majority

            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left_majority)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right_majority)

            return left_majority if left_count > right_count else right_majority

        return majority_element_rec(0, len(nums) - 1)

        # 摩尔投票法
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
            print(f"count: {count}, candidate: {candidate}, num: {num}")

        return candidate

        # 中间大的肯定是多数元素
        nums.sort()
        return nums[len(nums) // 2]

        # 哈希表
        hashtable = defaultdict(int)
        for num in nums:
            hashtable[num] += 1
            if hashtable[num] > len(nums) // 2:
                return num
# @lc code=end
solution = Solution()
solution.majorityElement(nums = [3,2,3])
print("---")
solution.majorityElement(nums = [2,2,1,1,1,2,2])
