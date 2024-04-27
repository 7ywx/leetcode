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

  - ***heapq.heapify(iterable)***:
    - 把一个可迭代对象 `iterable` 转换成一个合法的堆结构。

  - **heapq.nsmallest(n, iterable[, key])**:
    - 返回 `iterable` 中最小的 `n` 个元素组成的列表，使用堆排序算法实现高效查找。

  - **heapq.nlargest(n, iterable[, key])**:
    - 返回 `iterable` 中最大的 `n` 个元素组成的列表，同样使用堆排序算法实现高效查找。这两个函数均支持可选的 `key` 参数，用于指定元素比较时使用的函数。
- ### 8. 表示无穷大的方法
  - **math.inf**
  - **float('inf')**
  - **float('-inf')**
- ### 9. [zip(*iterables)](118.杨辉三角.py)
  - iterables：一个或多个可迭代对象。
  - 返回值：返回一个可迭代的 zip 对象，其中的元素为元组，每个元组包含来自各个可迭代对象中对应位置的元素。
- ### 10. [strip(string, chars=None)](8.字符串转换整数-atoi.py)
  - `string`: 待处理的字符串。
  - `chars` (可选): 一个指定要移除的字符集合（字符串），若未提供，则默认移除两侧的空白字符（包括空格、制表符、换行符等）。
  - 返回值：返回一个新的字符串，其中 `string` 两端的 `chars` 中指定的字符已被移除。若 `chars` 未提供，则返回去除两侧空白字符后的字符串。
- ### 11. [isdigit()](8.字符串转换整数-atoi.py)
  - **函数签名**: `str.isdigit()`
  - **说明**: `isdigit()` 是一个应用于字符串对象的方法，用于检查该字符串是否仅由数字组成（即0-9之间的ASCII字符）。该方法适用于需要验证输入字符串是否符合纯数字格式的场景。
  - **参数**: 无。`isdigit()`方法直接作用于调用它的字符串对象，无需额外传入参数。
  - **返回值**: 如果字符串中的所有字符都是数字，返回`True`；否则，返回`False`。即使字符串中包含非数字字符，只要有一个非数字字符存在，该方法就会返回`False`。
- ### 12.[collections.Counter([iterable-or-mapping]](15.三数之和.py)
  - 参数:
    - **iterable-or-mapping (可选)**: 一个可迭代对象（如列表、元组、字符串等）或映射（如字典）。如果提供此参数，`Counter` 会遍历其中的元素，计算每个元素的出现次数，并将结果存储在新创建的 `Counter` 对象中。如果不提供，将创建一个空的 `Counter`。
  - 主要方法和属性:
    - **`elements()`**: 返回一个迭代器，依次产出所有计数值非零的元素，每个元素出现的次数等于其计数值。

    - **`most_common([n])`**: 返回一个列表，包含 `Counter` 中最常见的元素及其计数值（按降序排列）。如果提供了整数参数 `n`，则仅返回前 `n` 个最常见的元素。

    - **`update([iterable-or-mapping])`**: 将一个可迭代对象或映射中的元素计数添加到当前 `Counter` 对象中。相当于逐一调用 `count()` 方法。

    - **`subtract([iterable-or-mapping])`**: 类似于 `update()`, 但将另一个可迭代对象或映射中的元素计数从当前 `Counter` 对象中减去。相当于逐一调用 `subtract()` 方法。

    - **`clear()`**: 清空 `Counter` 对象，删除所有计数。

    - **字典式操作**：可以像操作字典一样访问、修改、删除 `Counter` 中的元素。例如，可以通过 `counter[key]` 获取某个元素的计数，通过 `del counter[key]` 删除一个元素及其计数，以及使用 `in` 运算符检查元素是否存在。
- ### 13.[sequence.index(value, start, end)](33.搜索旋转排序数组.py)
  - sequence：可以是字符串、列表、元组等序列类型的实例。
  - value：要在序列中查找的元素值。
  - start（可选）：搜索的起始位置索引，默认为 0。
  - end（可选）：搜索的结束位置索引，默认为序列的长度，即搜索到序列的末尾。
  - 功能描述：该方法返回 value 在 sequence 中第一次出现的索引。如果 value 不在序列中，则会抛出 ValueError 异常。
  - 参数说明：start 和 end 参数允许你指定在序列的哪个子区间内进行搜索。注意，这些是包含性的，即 start 位置的元素和 end-1 位置的元素都会被考虑在内。
