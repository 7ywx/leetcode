import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:

import pandas as pd

trip_data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'client_id': [1, 2, 3, 4, 1, 2, 3, 2, 3, 4],
    'driver_id': [10, 11, 12, 13, 10, 11, 12, 12, 10, 13],
    'city_id': [1, 1, 6, 6, 1, 6, 6, 12, 12, 12],
    'status': ['completed', 'cancelled_by_driver', 'completed', 'cancelled_by_client', 'completed', 'completed', 'completed', 'completed', 'completed', 'cancelled_by_driver'],
    'request_at': ['2013-10-01', '2013-10-01', '2013-10-01', '2013-10-01', '2013-10-02', '2013-10-02', '2013-10-02', '2013-10-03', '2013-10-03', '2013-10-03'],
}

user_data = {
    'users_id': [1, 2, 3, 4, 10, 11, 12, 13, 1, 2],
    'banned': [None, 'Yes', None, None, None, None, None, None, None, 'No'],
    'role': ['client', 'client', 'client', 'client', 'driver', 'driver', 'driver', 'driver', 'client', 'driver'],
}

trips = pd.DataFrame(trip_data)
users = pd.DataFrame(user_data)
