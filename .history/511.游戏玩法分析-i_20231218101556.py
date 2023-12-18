import pandas as pd
def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
	['first_login'] = pd.to_datetime(df['event_date'])
	['first_login'] = .groupby('player_id')['first_login'].transform('min')
	.dropna(subset=['first_login'], inplace=True)
