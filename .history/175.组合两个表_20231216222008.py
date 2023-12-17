import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # 合并两个 DataFrame，假设索引是相同的
    return person.merge(address, how='left').drop(['personId','addressId'], axis=1)
import unittest


    unittest.main()
