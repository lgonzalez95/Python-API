class AccountInfo:

    def __init__(self, title, name, email, password, birth_date, birth_month, birth_year):
        self.title = title
        self.name = name
        self.email = email
        self.password = password
        self.birth_date = birth_date
        self.birth_month = birth_month
        self.birth_year = birth_year

    def __str__(self):
        return f"Title: {self.title}, Name: {self.name}, Email: {self.email}, Password: {self.password}"
