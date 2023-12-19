import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    array = []
    num_cols = len(logs.columns)
    print("len(logs) = " + str(len(logs.columns)))
    for index,row in logs.iterrows():
        if (index + 2 <= num_cols) & (num_cols > 1):
            print(index)
            next_row = logs.iloc[index + 1]
            next_two_row = logs.iloc[index + 2]
        else:
            break
        if (row.num == next_row.num) & (row.num == next_two_row.num):
            array.append(row.num)
        else:
            break
    return pd.DataFrame(array,columns=['ConsecutiveNums'])

data = {
    'id': [1, 2, 3, 4, 5, 6, 7],
    'num': [1, 1, 1, 2, 1, 2, 2]
}

data1 = {
    'id': [1, 2, 3],
    'num': [1, 1, 1]
}

df1 = pd.DataFrame(data)

df = pd.DataFrame(data)

print(consecutive_numbers(df1))
