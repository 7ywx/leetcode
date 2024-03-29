import pandas as pd
import datetime
def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    '''
    取消率 的计算方式如下：(被司机或乘客取消的非禁止用户生成的订单数量) / (非禁止用户生成的订单总数)。
    非禁止用户即 banned 为 No 的用户，禁止用户即 banned 为 Yes 的用户。其中取消率 Cancellation Rate 需要四舍五入保留 两位小数 。
    '''
    #trips = trips.merge(users, left_on=['driver_id','client_id'], right_on='users_id', how='inner')
    unbanned = []#True：非禁止用户，False：禁止用户
    uncount = 0
    for index,row in trips.iterrows():
        #row['banned'] = (users[users['users_id'] == row['client_id']]['banned'].values[0] == 'No') & (users[users['users_id'] == row['driver_id']]['banned'].values[0] == 'No')
        if (users[users['users_id'] == row['client_id']]['banned'].values[0] == 'No') & (users[users['users_id'] == row['driver_id']]['banned'].values[0] == 'No'):
            uncount += 1
        unbanned.append((users[users['users_id'] == row['client_id']]['banned'].values[0] == 'No') & (users[users['users_id'] == row['driver_id']]['banned'].values[0] == 'No'))
        #print((users[users['users_id'] == row['client_id']]['banned'].values[0]=='No'))
        #print((users[users['users_id'] == row['client_id']]['banned'].values[0] == 'No') & (users[users['users_id'] == row['driver_id']]['banned'].values[0] == 'No'))
    #trips['banned'] = (users[users['users_id'] == trips['client_id']]['banned'] == 'No') & (users[users['users_id'] == trips['driver_id']]['banned'] == 'No')
    trips['unbanned'] = unbanned
    tripsgy = trips[(trips['unbanned']==True)&(trips['request_at'].isin(['2013-10-01', '2013-10-02', '2013-10-03']))].groupby('request_at')
    Day=[]
    Cancellation=[]
    for name,group in tripsgy:
        print(name)
        print(group)
        print(group[group['status']!='completed'].shape[0])
        print(group.shape[0])
        cancellationRate = (group[group['status']!='completed'].shape[0]/group.shape[0])
        Day.append(group['request_at'].values[0])
        Cancellation.append(round((group[group['status']!='completed'].shape[0]/group.shape[0]),2))
        print('---')
    print(Cancellation)
    data = pd.DataFrame({
        'Day': ['2013-10-01', '2013-10-02', '2013-10-03'],
        'Cancellation Rate': Cancellation
    })
    print(data)
    return data

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    '''
    取消率 的计算方式如下：(被司机或乘客取消的非禁止用户生成的订单数量) / (非禁止用户生成的订单总数)。
    非禁止用户即 banned 为 No 的用户，禁止用户即 banned 为 Yes 的用户。其中取消率 Cancellation Rate 需要四舍五入保留 两位小数 。
    '''
    unbanned = []#True：非禁止用户，False：禁止用户
    for index,row in trips.iterrows():
        unbanned.append((users[users['users_id'] == row['client_id']]['banned'].values[0] == 'No') & (users[users['users_id'] == row['driver_id']]['banned'].values[0] == 'No'))
    trips['unbanned'] = unbanned
    tripsgy = trips[(trips['unbanned']==True)&(trips['request_at'].isin(['2013-10-01', '2013-10-02', '2013-10-03']))].groupby('request_at')
    Day=[]
    Cancellation=[]
    for name,group in tripsgy:
        Day.append(group['request_at'].values[0])
        Cancellation.append(round((group[group['status']!='completed'].shape[0]/group.shape[0]),2))
    data = pd.DataFrame({
        'Day': Day,
        'Cancellation Rate': Cancellation
    })
    return data

    # for index,row in trips.intertuples():
    #     if(row['request'])
    # UbGyrequest_at = trips[trips['unbanned']==True].groupby(['request_at']).size().reset_index(name='count')
    # #CancelledGyrequest_at = pd.DataFrame({'request_at':['2013-10-01', '2013-10-02', '2013-10-03'],'Cancellation Rate': [0.33, 0.00, 0.50]})
    # CancelledGyrequest_at = trips[(trips['status']!='completed' )&(trips['unbanned']==True)].groupby(['request_at']).size().reset_index(name='count')
    # for index,row in CancelledGyrequest_at.itertuples():

    # Cancellation = (CancelledGyrequest_at['count'] / UbGyrequest_at['count']).round(2)
    # print(Cancellation)
    # data = {'Day': ['2013-10-01', '2013-10-02', '2013-10-03'],
    #     'Cancellation Rate': [0.33, 0.00, 0.50]}
    # #ubNum = trips_gy_ru['count']
    # print(UbGyrequest_at)
    # print(CancelledGyrequest_at)
    #print(trips)

    # all = trips[(trips['request_at'].dt.date >= datetime.date(2013, 10, 1)) & (trips['request_at'].dt.date <= datetime.date(2013, 10, 3)) ]
    # cancelled_by_driver = all[all['status'] == 'cancelled_by_driver']
    # cancelled_by_client = all[all['status'] == 'cancelled_by_client']
    #print(all)
    # print(cancelled_by_driver)
    # print(cancelled_by_client)

trip_data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'client_id': [1, 2, 3, 4, 1, 2, 3, 2, 3, 4],
    'driver_id': [10, 11, 12, 13, 10, 11, 12, 12, 10, 13],
    'city_id': [1, 1, 6, 6, 1, 6, 6, 12, 12, 12],
    'status': ['completed', 'cancelled_by_driver', 'completed', 'cancelled_by_client', 'completed', 'completed', 'completed', 'completed', 'completed', 'cancelled_by_driver'],
    'request_at': pd.to_datetime(['2013-10-01', '2013-10-01', '2013-10-01', '2013-10-01', '2013-10-02', '2013-10-02', '2013-10-02', '2013-10-03', '2013-10-03', '2013-10-03']),
}

user_data = {
    'users_id': [1, 2, 3, 4, 10, 11, 12, 13],
    'banned': ['No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No'],
    'role': ['client', 'client', 'client', 'client', 'driver', 'driver', 'driver', 'driver']
}

trips = pd.DataFrame(trip_data)
users = pd.DataFrame(user_data)

trips_and_users(trips, users)
