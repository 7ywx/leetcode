import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:

data = {
    'id': [1, 2, 3],
    'email': ['john@example.com', 'bob@example.com', 'john@example.com']
}
df = pd.DataFrame(data)
