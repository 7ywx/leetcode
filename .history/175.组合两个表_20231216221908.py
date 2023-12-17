import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # 合并两个 DataFrame，假设索引是相同的
    return person.merge(address, how='left').drop(['personId','addressId'], axis=1)
import unittest

class TestCombineTwoTables(unittest.TestCase):

    def setUp(self):
        self.person = pd.DataFrame({'personId': [1, 2, 3],
                                    'name': ['John', 'Jane', 'Mike']})
        self.address = pd.DataFrame({'personId': [1, 2, 4],
                                     'address': ['123 Main St', '456 Elm St', '789 Oak St']})

    def test_combine_two_tables(self):
        result = combine_two_tables(self.person, self.address)
        expected = pd.DataFrame({'personId': [1, 2, 3],
                                 'name': ['John', 'Jane', 'Mike'],
                                 'address': ['123 Main St', '456 Elm St', '789 Oak St']})
        self.assertEqual(result.equals(expected), True)

if __name__ == '__main__':
    unittest.main()
