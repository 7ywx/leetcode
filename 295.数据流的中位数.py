#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
# https://leetcode.cn/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (54.19%)
# Likes:    968
# Dislikes: 0
# Total Accepted:    136.5K
# Total Submissions: 251.7K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
  '[[],[1],[2],[],[3],[]]'
#
# 中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。
#
#
# 例如 arr = [2,3,4] 的中位数是 3 。
# 例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
#
#
# 实现 MedianFinder 类:
#
#
#
# MedianFinder() 初始化 MedianFinder 对象。
#
#
# void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
#
#
# double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10^-5 以内的答案将被接受。
#
#
#
# 示例 1：
#
#
# 输入
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# 输出
# [null, null, null, 1.5, null, 2.0]
#
# 解释
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
#
# 提示:
#
#
# -10^5 <= num <= 10^5
# 在调用 findMedian 之前，数据结构中至少有一个元素
# 最多 5 * 10^4 次调用 addNum 和 findMedian
#
#
#

# @lc code=start
# class MedianFinder:

#     def __init__(self):
#         self.queMin = list()
#         self.queMax = list()

#     def addNum(self, num: int) -> None:
#         queMin_ = self.queMin
#         queMax_ = self.queMax

#         if not queMin_ or num <= -queMin_[0]:
#             heapq.heappush(queMin_, -num)
#             if len(queMax_) + 1 < len(queMin_):
#                 heapq.heappush(queMax_, -heapq.heappop(queMin_))
#         else:
#             heapq.heappush(queMax_, num)
#             if len(queMax_) > len(queMin_):
#                 heapq.heappush(queMin_, -heapq.heappop(queMax_))

#     def findMedian(self) -> float:
#         queMin_ = self.queMin
#         queMax_ = self.queMax

#         if len(queMin_) > len(queMax_):
#             return -queMin_[0]
#         return (-queMin_[0] + queMax_[0]) / 2



class MedianFinder:
    #TODO 消化吸收 写一个自己的版本
    def __init__(self):
        self.A = [] # 小顶堆，保存较大的一半
        self.B = [] # 大顶堆，保存较小的一半

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))

    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0



# from sortedcontainers import SortedList
# class MedianFinder:

#     def __init__(self):
#       self.nums = SortedList()

#     def addNum(self, num: int) -> None:
#       self.nums.add(num)

#     def findMedian(self) -> float:
#       numLength = len(self.nums)
#       if numLength % 2 == 0:
#         return (self.nums[numLength // 2 - 1] + self.nums[numLength // 2]) / 2
#       else:
#         return self.nums[numLength // 2]

# class MedianFinder:
#     #TODO SortedList()

#     def __init__(self):
#       self.arr = []
#     def addNum(self, num: int) -> None:
#       self.arr.append(num)

#     def findMedian(self) -> float:
#       arrLength = len(self.arr)
#       self.arr.sort()
#       if arrLength % 2 == 0:
#         return (self.arr[arrLength // 2] + self.arr[arrLength // 2 - 1]) / 2
#       else:
#         return self.arr[arrLength // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
