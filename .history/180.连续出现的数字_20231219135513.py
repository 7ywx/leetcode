import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    count = 0
    for index,row in logs.iterrows():
        if index + 2 < len(logs):
        	next_row = logs.iloc[index + 1]
			next_two_row = logs.iloc[index + 2]
        if (row.num == next_row.num) & (row.num == next_two_row.num):

        else:
            count = 0


data = {
    'id': [1, 2, 3, 4, 5, 6, 7],
    'num': [1, 1, 1, 2, 1, 2, 2]
}

df = pd.DataFrame(data)

consecutive_numbers(df)
