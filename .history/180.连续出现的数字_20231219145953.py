import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    array = []
    num_cols = logs.shape[0]
    for index,row in logs.iterrows():
        if (index + 2 <= num_cols) and (num_cols > 1):
            next_row = logs.iloc[index + 1]
            next_two_row = logs.iloc[index + 2]
        else:
            consecutive_nums = pd.DataFrame(array,columns=['ConsecutiveNums'])
            consecutive_nums = consecutive_nums.drop_duplicates(subset=["ConsecutiveNums"]) #去重
            return  consecutive_nums
        if (row.num == next_row.num) and (row.num == next_two_row.num):
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
