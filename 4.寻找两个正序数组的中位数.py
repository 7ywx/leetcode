#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
# https://leetcode.cn/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (41.82%)
# Likes:    6956
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 2.5M
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
#
# 算法的时间复杂度应该为 O(log (m+n)) 。
#
#
#
# 示例 1：
#
#
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#
#
# 示例 2：
#
#
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#
#
#
#
#
#
# 提示：
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#

# @lc code=start
from typing import Optional
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        #装逼写法
        nums3, l = sorted(nums1 + nums2), len(nums1) + len(nums2)
        return nums3[l >> 1] if l & 1 else (nums3[(l >> 1) - 1] + nums3[l >> 1] ) / 2.0
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #暴力写法
        num=nums1+nums2
        num.sort()
        n=len(num)
        if n%2==1:
            return num[n//2]
        else:
            return (num[n//2]+num[n//2-1])/2
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKth(nums1: List[int], nums2: List[int], k: int) -> int:
            t,n,i,j = 0,0,0,0
            while True:
                if i == len(nums1):
                    return nums2[j+k-n-1]
                if j == len(nums2):
                    return nums1[i+k-n-1]
                if nums1[i] < nums2[j]:
                    i += 1
                    n += 1
                    t = 1
                else:
                    j += 1
                    n += 1
                    t = 2
                if n == k:
                    return nums1[i-1] if t == 1 else nums2[j-1]
        length = len(nums1) + len(nums2)
        if length % 2 == 1:
            #taget = length // 2 + 1
            return findKth(nums1, nums2, length // 2 + 1)
        else:
            #taget = length // 2 , length // 2 + 1
            return float((findKth(nums1, nums2, length // 2) + findKth(nums1, nums2, length // 2 + 1))) / 2
# @lc code=end
solution = Solution()
print(solution.findMedianSortedArrays([1,2], [3,4]))
