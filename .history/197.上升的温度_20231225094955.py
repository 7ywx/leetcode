import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['datetime'] = pd.to_datetime(weather['recordDate'])
    indexs = []
    for index,row in weather.iterrows():
        yesterday = row.datetime - pd.Timedelta(days=1)
        wY = weather[weather.datetime == yesterday]
        if (not wY.empty) and (row.temperature > wY.temperature.values):
            indexs.append(index)
    return weather.iloc[indexs][['id']]

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    df = weather.sort_values(by="recordDate", ascending=True)
    df["last_d"] = df["recordDate"].shift(1)
    df["last_t"] = df["temperature"].shift(1)
    df = df.loc[(df["recordDate"] - df["last_d"] == datetime.timedelta(days=1))
                & (df["temperature"] > df["last_t"])][["id"]]
    return df


weather_df = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'recordDate': ['2015-01-01', '2015-01-02', '2015-01-03', '2015-01-04'],
    'temperature': [10, 25, 20, 30]
})
rising_temperature(weather_df)
