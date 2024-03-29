# Python 语法和常用函数备忘录

## Python 语法

- ### 1. [```if target - num in hashtable```](1.两数之和.cpp):
- 在 ```if a in hashtable:``` 这样的条件判断中，Python会检查字典（哈希表）hashtable 的键（keys）中是否包含变量 a。也就是说，它不会查找值（values），而是查找键。

- ### 2. 列表推导式
`[expression for item in iterable if condition]`
- **expression**：一个表达式，用于计算每个 item 应该在新列表中的值。
- **item**：迭代变量，在遍历 iterable 时的当前项。
- **iterable**：任意可迭代对象，如列表、元组、字符串或生成器等。
- **if condition**：可选条件，仅当此条件为 True 时，当前 item 才会被包含在新列表中。

- ### 3. //
- `//` 是一个 floor division（向下取整除法）运算符。它用于两个数之间的除法计算，并返回商的整数部分，忽略任何小数点后的部分，且结果总是小于或等于真实商。

## Python 常用函数
- ### 1. enumerate(iterable, start=0)
  - iterable：必需参数，接受任何可迭代对象。
  - start：可选参数，默认为0，指定枚举开始的索引值。
  - 用途：
    1. 当你需要在处理数据集合时不仅知道当前元素，还需要知道其在序列中的确切位置（索引）时，enumerate() 函数就显得尤为重要。
    2. 它允许你在循环中以一种简洁的方式结合索引和值进行操作。
- ### 2. [divmod(a, b)](2.两数相加.py)
  - a: 被除数
  - b: 除数
  - `divmod(a, b)` 函数会将两个数字进行整除运算，并以元组形式返回商和余数。

- ### 3. [separator.join(iterable)](6.n-字形变换.py)
  - iterable：可迭代对象，如列表、元组、字符串或生成器等。
  - separator：可选参数，默认为' '，用于分隔各个元素。
  - `str.join()` 是一个字符串方法，用于将一个可迭代对象（通常为列表、元组或其他序列）中所有元素连接成一个字符串，并在每个元素之间插入指定的分隔符。

- ### 4. [abs(x)](7.整数反转.py)
  - x：可选参数，默认为0，表示要计算绝对值的数字。
  - abs() 函数是 Python 中的一个内置函数，用于计算数字的绝对值（absolute）。

- ### 5. [reduce(function, iterable[, initializer])](136.只出现一次的数字.py)
  - function：表示要执行的函数。
  - iterable：表示要迭代的可迭代对象。
  - initializer：可选参数，表示初始值。如果提供了这个参数，那么在计算时会从这个初始值开始迭代，否则就从序列的第一个元素和第二个元素开始计算。

- ### 6. [list.index(value, start=0, stop=(len(list)))](33.搜索旋转排序数组.py)
  - value：要查找的值。
  - start：可选参数，默认为0，表示要搜索的起始位置。
  - stop：可选参数，默认为len(list)，表示要搜索的结束位置。

- ### 7. heapq 模块函数

  - **heapq.heappush(heap, item)**:
    - 将元素 `item` 推入堆 `heap` 中，同时保持堆的特性（对于最小堆来说，堆顶元素始终是最小的）。

  - **heapq.heappop(heap)**:
    - 移除并返回堆 `heap` 中最小的元素。对于默认的小顶堆，就是堆顶元素。

  - **heapq.heappushpop(heap, item)**:
    - 先将 `item` 推入堆 `heap` 中，然后立即弹出并返回堆中最小的元素。

  - **heapq.heapify(iterable)**:
    - 把一个可迭代对象 `iterable` 转换成一个合法的堆结构。

  - **heapq.nsmallest(n, iterable[, key])**:
    - 返回 `iterable` 中最小的 `n` 个元素组成的列表，使用堆排序算法实现高效查找。

  - **heapq.nlargest(n, iterable[, key])**:
    - 返回 `iterable` 中最大的 `n` 个元素组成的列表，同样使用堆排序算法实现高效查找。这两个函数均支持可选的 `key` 参数，用于指定元素比较时使用的函数。
- ### 8. 表示无穷大的方法
  - **math.inf**
  - **float('inf')**
  - **float('-inf')**
