import random

def monkey_sort(arr):
    n = 0
    while not is_sorted(arr) and  n < 1000:
        # 随机选择两个不同的元素进行交换
        i, j = random.sample(range(len(arr)), 2)
        arr[i], arr[j] = arr[j], arr[i]
        print(f"第{n+1}次: {arr}")
        n += 1

    return arr

def is_sorted(arr):
    # 检查数组是否已按升序排列
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

# 示例用法：
unsorted_arr = [5, 3, 8, 4, 2]
sorted_arr = monkey_sort(unsorted_arr.copy())
print(sorted_arr)
