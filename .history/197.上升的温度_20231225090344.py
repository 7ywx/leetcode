import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # 找出与之前（昨天的）日期相比温度更高的所有日期的 id 。
    weather['datatime'] = pd.to_datetime(weather['recordDate'])
    for index, row in weather.iterrows():
        yesterday = pd.to_datetime(row.recordDate).shift(periods=1)
        print(yesterday)
    print(weather)


weather_df = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'recordDate': ['2015-01-01', '2015-01-02', '2015-01-03', '2015-01-04'],
    'Temperature': [10, 25, 20, 30]
})
# 创建一个包含日期的Series
dates = pd.Series(['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'])

# 将字符串转换为datetime对象
date_objs = pd.to_datetime(dates)

# 将日期向前移动一天
yesterday = date_objs.shift(periods=1)

# 打印结果
print(yesterday)
rising_temperature(weather_df)
