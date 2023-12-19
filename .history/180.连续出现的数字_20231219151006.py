import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    array = []
    num_cols = logs.shape[0]
    for index,row in logs.iterrows():
        if (index + 2 < num_cols) and (num_cols > 1):
            next_row = logs.iloc[index + 1]
            next_two_row = logs.iloc[index + 2]
        else:
            consecutive_nums = pd.DataFrame(array,columns=['ConsecutiveNums'])
            return  consecutive_nums
        if (row.num == next_row.num) and (row.num == next_two_row.num):
            array.append(row.num)

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    if not isinstance(logs, pd.DataFrame):
        raise ValueError("logs must be a pandas DataFrame")

    logs = logs.sort_values(by='num', ascending=False)

    unique_nums = logs['num'].unique()

    if len(unique_nums) != len(logs['num']):
        # 如果数字不是连续的，则返回空的 DataFrame
        return pd.DataFrame(columns=['ConsecutiveNums'])

    # 找到连续的数字
    consecutive_nums = logs[logs['num'].diff() == 1]['num'].tolist()

    return pd.DataFrame(consecutive_nums, columns=['ConsecutiveNums'])
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

print(consecutive_numbers(df1))
