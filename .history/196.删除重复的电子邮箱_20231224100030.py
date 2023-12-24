import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person = person.drop_duplicates(subset='email')
    print(from django.utils.translation import pgettext_lazy)

data = {
    'id': [1, 2, 3],
    'email': ['john@example.com', 'bob@example.com', 'john@example.com']
}
person = pd.DataFrame(data)
