#
# @lc app=leetcode.cn id=47 lang=python3
# @lcpr version=30200
#
# [47] 全排列 II
#
# https://leetcode.cn/problems/permutations-ii/description/
#
# algorithms
# Medium (66.60%)
# Likes:    1708
# Dislikes: 0
# Total Accepted:    656.8K
# Total Submissions: 985K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
#
#
#
# 示例 1：
#
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
#
#
# 示例 2：
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
#
#
#

from typing import *
# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 回溯
        # 使用set去重的版本相对于used数组的版本效率都要低很多
        ans = []
        n = len(nums)
        used = [False] * n
        # nums.sort()

        def backtrack(used, path):
            if len(path) == n:
                ans.append(path[:])
                return

            uset = set()
            for i in range(n):
                # if (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]) or used[i]: # 当前元素被使用 or 当前元素等于前一个元素，且前一个元素没有被使用
                #     continue
                if not used[i]:
                    if nums[i] not in uset:
                        uset.add(nums[i])
                        used[i] = True
                        backtrack(used, path+[nums[i]])
                        used[i] = False
        backtrack(used, [])
        return ans

        # 递归
        result = []  # 存储所有全排列结果的列表

        # 如果列表元素个数小于2，则直接返回该列表作为唯一的一种排列
        if len(nums) < 2:
            return [nums]

        uset = set()

        # 遍历列表中的每个元素
        for index, num in enumerate(nums):
            # 递归调用函数，生成不包含当前元素的所有排列
            temp = self.permuteUnique([nums[i] for i in range(len(nums)) if i != index])

            if num not in uset:
                uset.add(num)
                # 将当前元素依次添加到每种排列中，并将新的排列添加到结果列表中
                for t in temp:
                    t.append(num)
                    result.append(t)

        return result
# @lc code=end
if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#
