import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id',ascending=True,inplace=True).
    person.drop_duplicates(subset='email',keep='first',inplace=True)
    print(person)


data = {
    'id': [1, 2, 3],
    'email': ['john@example.com', 'bob@example.com', 'john@example.com']
}
person = pd.DataFrame(data)

df = pd.DataFrame({
	'id': [10, 15, 5, 20],
	'email': ['john@example.com', 'bob@example.com', 'john@example.com', 'bob@example.com']
 })
delete_duplicate_emails(df)
