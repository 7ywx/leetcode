import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    count = 0
    for row in logs.itertuples():
		row+1.num


data = {
    'id': [1, 2, 3, 4, 5, 6, 7],
    'num': [1, 1, 1, 2, 1, 2, 2]
}

df = pd.DataFrame(data)

consecutive_numbers(df)
