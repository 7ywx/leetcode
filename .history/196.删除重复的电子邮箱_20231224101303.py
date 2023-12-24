import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.drop_duplicates(subset='email',keep='first'inplace=True)
    print(person)
    # return person


data = {
    'id': [1, 2, 3],
    'email': ['john@example.com', 'bob@example.com', 'john@example.com']
}
person = pd.DataFrame(data)
delete_duplicate_emails(person)
