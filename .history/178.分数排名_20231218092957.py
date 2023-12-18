import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:

	df['rank'] = scores['score'].rank(method='first', ascending=False)
