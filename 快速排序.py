# hoare
def hoare_partition(arr, low, high):
    pivot = arr[low]  # 选择第一个元素作为基准
    left = low - 1
    right = high + 1

    while True:
        # 找到左边第一个大于或等于基准的元素
        left += 1
        while arr[left] < pivot:
            left += 1

        # 找到右边第一个小于或等于基准的元素
        right -= 1
        while arr[right] > pivot:
            right -= 1

        # 如果左右指针相遇或交错，返回右指针的位置
        if left >= right:
            return right

        # 交换左右指针找到的元素
        arr[left], arr[right] = arr[right], arr[left]

def quicksort_hoare(arr, low, high):
    if low < high:
        p = hoare_partition(arr, low, high)
        quicksort_hoare(arr, low, p)    # 对左半部分递归
        quicksort_hoare(arr, p + 1, high)  # 对右半部分递归

# 示例
arr = [3, 6, 8, 10, 1, 2, 1]
quicksort_hoare(arr, 0, len(arr) - 1)
print(arr)

# 挖坑法
def quicksort_dig(arr, low, high):
    if low >= high:
        return

    # 选择基准元素
    pivot = arr[low]
    i, j = low, high

    while i < j:
        # 从右向左找第一个小于基准的元素
        while i < j and arr[j] >= pivot:
            j -= 1
        # 将右边找到的小于基准的元素填到左边的坑中
        if i < j:
            arr[i] = arr[j]
            i += 1

        # 从左向右找第一个大于基准的元素
        while i < j and arr[i] <= pivot:
            i += 1
        # 将左边找到的大于基准的元素填到右边的坑中
        if i < j:
            arr[j] = arr[i]
            j -= 1

    # 最后把基准元素放入i == j的位置
    arr[i] = pivot

    # 递归排序左右两部分
    quicksort_dig(arr, low, i - 1)
    quicksort_dig(arr, i + 1, high)

# 示例
arr = [3, 6, 8, 10, 1, 2, 1]
quicksort_dig(arr, 0, len(arr) - 1)
print(arr)

# 三数取中
def median_of_three(arr, low, high):
    mid = (low + high) // 2
    # 比较arr[low], arr[mid], arr[high]并找出中位数
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    # 中位数现在位于arr[mid]，我们交换到arr[low]作为基准
    arr[low], arr[mid] = arr[mid], arr[low]
    return arr[low]

def partition(arr, low, high):
    pivot = median_of_three(arr, low, high)
    i = low
    j = high
    while True:
        # 从左到右找到比基准大的元素
        while i < j and arr[i] < pivot:
            i += 1
        # 从右到左找到比基准小的元素
        while j > i and arr[j] > pivot:
            j -= 1
        if i >= j:
            break
        # 交换元素
        arr[i], arr[j] = arr[j], arr[i]
    return j

def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)   # 排序左子数组
        quicksort(arr, p + 1, high)  # 排序右子数组

# 示例
arr = [3, 6, 8, 10, 1, 2, 1]
quicksort(arr, 0, len(arr) - 1)
print(arr)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # 选择中间元素作为基准
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# 示例
arr = [3, 6, 8, 10, 1, 2, 1]
print(quicksort(arr))

# 常见
def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        # right找小于key的
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right] # 小于key放left

        # left找大于key的
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left] # 大于key放right

    array[right] = key # 确定key的位置
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)

# 算法导论
def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)

def partition(array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i+1]
    return i + 1

# 用栈实现的
def quick_sort(array, l, r):
    if l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])

s = [4,5,3,7,2,2,3]
quick_sort(s,0,6)
print(s)
