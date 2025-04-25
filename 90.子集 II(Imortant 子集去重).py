#
# @lc app=leetcode.cn id=90 lang=python3
# @lcpr version=30200
#
# [90] 子集 II
#
# https://leetcode.cn/problems/subsets-ii/description/
#
# algorithms
# Medium (63.97%)
# Likes:    1304
# Dislikes: 0
# Total Accepted:    448.9K
# Total Submissions: 701.6K
# Testcase Example:  '[1,2,2]'
#
# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的 子集（幂集）。
#
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
#
#
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#
#
# 示例 2：
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
#
#
#
#
#

from typing import *
# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        def backtrack(start, path):
            ans.append(path[:])
            uset = set()
            for i in range(start, n):
                if nums[i] in uset:
                    continue
                uset.add(nums[i])
                backtrack(i+1, path+[nums[i]])
        backtrack(0, [])
        return ans
# @lc code=end
if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#
