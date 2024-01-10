import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id',ascending=True)
    print(person)
    person.drop_duplicates(subset='email', keep='first', inplace=True)
    # return person


data = {
    'id': [1, 2, 3],
    'email': ['john@example.com', 'bob@example.com', 'john@example.com']
}
person = pd.DataFrame(data)

df = pd.DataFrame({
    'email': ['test1@example.com', 'test2@example.com', 'test1@example.com', 'test3@example.com'],
	'id': [10, 15, 5, 20]
 })
delete_duplicate_emails(person)
