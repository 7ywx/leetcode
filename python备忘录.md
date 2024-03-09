# Python 语法和常用函数备忘录

## Python 语法

### 1. [```if target - num in hashtable```](1.两数之和.cpp):
- 在 ```if a in hashtable:``` 这样的条件判断中，Python会检查字典（哈希表）hashtable 的键（keys）中是否包含变量 a。也就是说，它不会查找值（values），而是查找键。

### 2. 列表推导式
`[expression for item in iterable if condition]`
- **expression**：一个表达式，用于计算每个 item 应该在新列表中的值。
- **item**：迭代变量，在遍历 iterable 时的当前项。
- **iterable**：任意可迭代对象，如列表、元组、字符串或生成器等。
- **if condition**：可选条件，仅当此条件为 True 时，当前 item 才会被包含在新列表中。

## Python 常用函数
### 1. enumerate(iterable, start=0)
- iterable：必需参数，接受任何可迭代对象。
- start：可选参数，默认为0，指定枚举开始的索引值。
- 用途：
  1. 当你需要在处理数据集合时不仅知道当前元素，还需要知道其在序列中的确切位置（索引）时，enumerate() 函数就显得尤为重要。
  2. 它允许你在循环中以一种简洁的方式结合索引和值进行操作。
### 2. [divmod(a, b)](2.两数相加.py)
- a: 被除数
- b: 除数
- 用途：
	- `divmod(a, b)` 函数会将两个数字进行整除运算，并以元组形式返回商和余数。
