import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['datetime'] = pd.to_datetime(weather['recordDate'])
    indexs = []
    for index,row in weather.iterrows():
        #yesterday = row.datetime - pd.Timedelta(days=1)
        yesterday = row.datetime.shift(days=-1)
        wY = weather[weather.datetime == yesterday]
        if (not wY.empty) and (row.temperature > wY.temperature.values):
            indexs.append(index)
    return weather.iloc[indexs][['id']]

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    '''输入：
Weather 表：
+----+------------+-------------+
| id | recordDate | Temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
输出：
+----+
| id |
+----+
| 2  |
| 4  |
+----+
解释：
2015-01-02 的温度比前一天高（10 -> 25）
2015-01-04 的温度比前一天高（20 -> 30）
'''


weather_df = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'recordDate': ['2015-01-01', '2015-01-02', '2015-01-03', '2015-01-04'],
    'temperature': [10, 25, 20, 30]
})
rising_temperature(weather_df)
