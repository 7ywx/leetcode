import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    for index, row in logs.itertuples():
    print(index, row)


data = {
    'id': [1, 2, 3, 4, 5, 6, 7],
    'num': [1, 1, 1, 2, 1, 2, 2]
}

df = pd.DataFrame(data)

consecutive_numbers(df)
