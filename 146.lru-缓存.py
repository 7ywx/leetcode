#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#
# https://leetcode.cn/problems/lru-cache/description/
#
# algorithms
# Medium (53.69%)
# Likes:    3082
# Dislikes: 0
# Total Accepted:    588.8K
# Total Submissions: 1.1M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
#
# 实现 LRUCache 类：
#
#
#
#
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组
# key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
#
#
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
#
#
#
#
#
# 示例：
#
#
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
#
#
#
#
# 提示：
#
#
# 1 <= capacity <= 3000
# 0 <= key <= 10000
# 0 <= value <= 10^5
# 最多调用 2 * 10^5 次 get 和 put
#
#
#

#标签 OrderedDict
# @lc code=start
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity # 容量
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 将 key 变为最近使用
        self.cache.move_to_end(key) # 后面的表示为最近使用
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 修改 key 的值
            self.cache[key] = value
            # 将 key 变为最近使用
            self.cache.move_to_end(key)
            return

        if len(self.cache) >= self.cap:
            # 链表头部就是最久未使用的 key
            self.cache.popitem(last=False)
        # 将新的 key 添加链表尾部
        self.cache[key] = value
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
