import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
	rank['rank'] = scores['score'].rank(method='first', ascending=False)
