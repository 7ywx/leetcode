import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    # 定义一个空数组
    array = []
    # 获取数据框的行数
    num_cols = logs.shape[0]

    # 遍历数据框的每一行
    for index, row in logs.iterrows():
        # 判断是否还有下一行和下下一行数据
        if (index + 2 < num_cols) and (num_cols > 1):
            # 获取下一行和下下一行数据
            next_row = logs.iloc[index + 1]
            next_two_row = logs.iloc[index + 2]
        else:
            # 如果还有剩余的行数不足三行，则返回已经找到的连续数字数据
            consecutive_nums = pd.DataFrame(array, columns=['ConsecutiveNums'])
            return consecutive_nums

        # 判断当前行、下一行和下下一行的数字是否相等
        if (row.num == next_row.num) and (row.num == next_two_row.num):
            # 将相等的数字添加到数组中
            array.append(row.num)

data = {
    'id': [1, 2, 3, 4, 5, 6, 7],
    'num': [1, 1, 1, 2, 1, 2, 2]
}

data1 = {
    'id': [1],
    'num': [1]
}

df1 = pd.DataFrame(data1)

df = pd.DataFrame(data)

print(consecutive_numbers(df))
