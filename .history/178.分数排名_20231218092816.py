import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    score_sorted_desc = scores.sort_values(by=['score'], ascending=False)
	df['rank'] = df['score'].rank(method='first', ascending=False)

