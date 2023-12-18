import pandas as pd
def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
	df['first_login'] = pd.to_datetime(df['event_date'])
df['first_login'] = df.groupby('player_id')['first_login'].transform('min')
df.dropna(subset=['first_login'], inplace=True)
