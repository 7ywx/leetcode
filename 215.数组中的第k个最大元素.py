#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode.cn/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (61.72%)
# Likes:    2432
# Dislikes: 0
# Total Accepted:    1M
# Total Submissions: 1.7M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
#
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
#
#
# 示例 1:
#
#
# 输入: [3,2,1,5,6,4], k = 2
# 输出: 5
#
#
# 示例 2:
#
#
# 输入: [3,2,3,1,2,4,5,5,6], k = 4
# 输出: 4
#
#
#
# 提示：
#
#
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#
from typing import List
import random
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 快速选择算法
        def quick_select(nums, k):
            # 随机选择基准数
            pivot = random.choice(nums)
            big, equal, small = [], [], []
            # 将大于、小于、等于 pivot 的元素划分至 big, small, equal 中
            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)
            if k <= len(big):
                # 第 k 大元素在 big 中，递归划分
                return quick_select(big, k)
            if len(nums) - len(small) < k:
                # 第 k 大元素在 small 中，递归划分
                return quick_select(small, k - len(nums) + len(small))
            # 第 k 大元素在 equal 中，直接返回 pivot
            return pivot

        return quick_select(nums, k)


        # return heapq.nlargest(k, nums)[-1]

        # 小顶堆，堆顶是最小元素
        pq = []
        for e in nums:
            # 每个元素都要过一遍二叉堆
            heapq.heappush(pq, e)
            # 堆中元素多于 k 个时，删除堆顶元素
            if len(pq) > k:
                heapq.heappop(pq)
        # pq 中剩下的是 nums 中 k 个最大元素，
        # 堆顶是最小的那个，即第 k 个最大元素
        return pq[0]
# @lc code=end
# nums = [5,3,6,4,1,2,8,7]
# def QuickSort(num):
#  if len(num) <= 1: #边界条件
#   return num
#  key = num[0] #取数组的第一个数为基准数
#  llist,rlist,mlist = [],[],[key] #定义空列表，分别存储小于/大于/等于基准数的元素
#  for i in range(1,len(num)): #遍历数组，把元素归类到3个列表中
#   if num[i] > key:
#    rlist.append(num[i])
#   elif num[i] < key:
#    llist.append(num[i])
#   else:
#    mlist.append(num[i])
#  return QuickSort(llist)+mlist+QuickSort(rlist) #对左右子列表快排，拼接3个列表并返回
# print(QuickSort(nums))

def quick_sort_hoare(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = partition_hoare(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort_hoare(arr, low, pi)
        quick_sort_hoare(arr, pi + 1, high)

def partition_hoare(arr, low, high):
    # Choose the middle element as pivot
    pivot = arr[random.randint(low, high)] # arr[(low + high) // 2]
    i = low - 1
    j = high + 1

    while True:
        # Move i to the right until finding an element that is greater than or equal to the pivot
        i += 1
        while arr[i] < pivot:
            i += 1

        # Move j to the left until finding an element that is less than or equal to the pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # If the pointers have crossed, partitioning is done
        if i >= j:
            return j

        # Swap elements at i and j
        arr[i], arr[j] = arr[j], arr[i]

# 示例数组
example_array = [10, 7, 8, 9, 1, 5]
# 调用快速排序函数
quick_sort_hoare(example_array, 0, len(example_array) - 1)
print("Sorted array:", example_array)
