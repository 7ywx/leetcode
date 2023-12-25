import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    print(weather_df)

weather_df = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'recordDate': ['2015-01-01', '2015-01-02', '2015-01-03', '2015-01-04'],
    'Temperature': [10, 25, 20, 30]
})
rising_temperature(weather_df)
