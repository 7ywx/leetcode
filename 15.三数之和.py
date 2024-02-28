#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode.cn/problems/3sum/description/
#
# algorithms
# Medium (37.62%)
# Likes:    6658
# Dislikes: 0
# Total Accepted:    1.6M
# Total Submissions: 4.3M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j !=
# k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
#
# 你返回所有和为 0 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
#
#
# 示例 2：
#
#
# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
#
#
# 示例 3：
#
#
# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。
#
#
#
#
# 提示：
#
#
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#
#
from typing import Optional
from typing import List
from collections import Counter
import bisect
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums) # 后续可以通过 count[num] 来快速获取某个元素 num 在列表中出现的次数
        st = sorted(count)  # 键由小到大排序(nums去重后排序)
        res=list()
        for i,num in enumerate(st): # i:索引，num:元素值
            if count[num] > 1: # 有重复元素
                if num == 0 and count[num] > 2: # 有三个0
                    res.append([0,0,0])
                elif (k:= -num*2) in count:
                    res.append([num,num,k])   # 有两个数一样
            if num < 0: # 三个数都不一样的（由于st是递增的，当num为正数时，三数之和不可能为0）
                left = bisect.bisect_left(st,-num-st[-1],i+1) # st[-1]: st最大值, x: st中能使三数和为0的最小可能数(num + st[-1] + x = 0), left: st中第一个>=num-st[-1]的索引
                # right为什么是-num//2? 答：st是递增的，如果j > -num//2 j就不是第二个数
                right = bisect.bisect(st,-num//2,left) # -num//2: st中能使三数和为0的最大可能数(num + y + y = 0), right: st中第一个>num//2的索引
                for j in st[left:right]: # j是第二个数可能的范围
                    if (k:=-num-j) in count and k != j: # k存在且k != j (num+j+k=0，这里要找的是三个数都不一样的，所以要加上k!=j)
                        res.append([num,j,k])
        return res
# @lc code=end
solution = Solution()
solution.threeSum([-1,0,1,2,-1,-4])
# solution.threeSum([0,1,1])
