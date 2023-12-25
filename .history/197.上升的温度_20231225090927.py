import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # 找出与之前（昨天的）日期相比温度更高的所有日期的 id 。
    weather['datatime'] = pd.to_datetime(weather['recordDate'])
    for index,row in weather.iterrows():
        print(row.datatime)
        #yesterday = row.datatime.shift(periods=1)
        # print(yesterday)
    print(weather)


weather_df = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'recordDate': ['2015-01-01', '2015-01-02', '2015-01-03', '2015-01-04'],
    'Temperature': [10, 25, 20, 30]
})
rising_temperature(weather_df)
