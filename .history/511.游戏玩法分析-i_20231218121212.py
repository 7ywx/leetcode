import pandas as pd
def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
	# 将活动表中的 'event_date' 列转换为日期时间格式，并将结果赋值给 'activity' 字典中的 'first_login' 键
	activity['first_login'] = pd.to_datetime(activity['event_date'])
	# 对于每个 'player_id'，找到最早的 'first_login' 日期时间，并将结果赋值给 'activity' 字典中的 'first_login' 键
	activity['first_login'] = activity.groupby('player_id')['first_login'].transform('min')
	# 删除重复的活动行，只保留 'player_id' 列和 'first_login' 列的第一行
	activity.drop_duplicates(subset=['player_id'],keep='first',inplace=True)
	# 返回活动表中 'player_id' 列和 'first_login' 列的数据
	print(1)
	return activity[['player_id', 'first_login']]
def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # 按照player_id分组，对event_date取最小值，然后重置索引
    activity = activity.groupby('player_id')['event_date'].min().reset_index()
    # 将活动表的列名event_date修改为first_login
    activity.rename(columns={'event_date':'first_login'},inplace=True)
    # 返回修改后的活动表
    """
    在这个例子中，函数game_analysis被定义了两次。
    当调用game_analysis(df)时，它实际上调用了第二个game_analysis函数，而忽略了第一个函数。
    这种现象被称为函数重载，但是在这个例子中，两个函数的参数和返回值是相同的，唯一的区别是函数的实现。
    因此，Python根据函数的参数类型和名称来区分不同的函数重载版本。
    在这种情况下，Python根据函数的定义顺序来确定调用哪个函数。
    第一个game_analysis函数在第二个game_analysis函数的前面定义，所以当使用相同的参数调用时，它将被忽略，Python将自动调用后续定义的函数。
    """
    print(2)
    return activity

data = {'player_id': [1, 1, 2, 3, 3],
        'device_id': [2, 2, 3, 1, 4],
        'event_date': ['2016-03-01', '2016-05-02', '2017-06-25', '2016-03-02', '2018-07-03'],
        'games_played': [5, 6, 1, 0, 5]}

df = pd.DataFrame(data)
game_analysis(df)
#print(game_analysis(df))
