import pandas as pd
def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
	activity['first_login'] = pd.to_datetime(activity['event_date'])
	activity['first_login'] = activity.groupby('player_id')['first_login'].transform('min')
	print(df)
    activity['last_login'] = pd.to_datetime(activity['event_date'])
	activity.drop_duplicates(subset=['player_id'],keep='first',inplace=True)
	print(df)
	return activity


data = {'player_id': [1, 1, 2, 3, 3],
        'device_id': [2, 2, 3, 1, 4],
        'event_date': ['2016-03-01', '2016-05-02', '2017-06-25', '2016-03-02', '2018-07-03'],
        'games_played': [5, 6, 1, 0, 5]}

df = pd.DataFrame(data)

game_analysis(df)
