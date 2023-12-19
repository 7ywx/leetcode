import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    array = []
    for index,row in logs.iterrows():
        if index + 2 < len(logs):
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

df = pd.DataFrame(data)

print(consecutive_numbers(df))
