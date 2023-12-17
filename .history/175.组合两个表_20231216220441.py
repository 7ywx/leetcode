import pandas as pd
def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    for PersonId in person.iterrows():
        for AddressId in address.iterrows():
            if PersonId[1]['PersonId'] == AddressId[1]['PersonId']:
                person.loc[person['PersonId'] == PersonId[1]['PersonId'], 'AddressId'] = AddressId[1]['AddressId']
