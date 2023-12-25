import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # 找出与之前（昨天的）日期相比温度更高的所有日期的 id 。
    weather['datetime'] = pd.to_datetime(weather['recordDate'])
    ids = []
    indexs = []
    for index,row in weather.iterrows():
        yesterday = row.datetime - pd.Timedelta(days=1)
        wY = weather[weather.datetime == yesterday]
        if (not wY.empty) and (row.Temperature > wY.Temperature.values[0]):
            ids.append(row.id)
            indexs.append(index)
    print(indexs)
    print(weather.iloc[indexs][['id']])
    return weather.iloc[indexs][['id']]
    #print(weather)


weather_df = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'recordDate': ['2015-01-01', '2015-01-02', '2015-01-03', '2015-01-04'],
    'Temperature': [10, 25, 20, 30]
})
rising_temperature(weather_df)
