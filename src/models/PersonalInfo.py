class PersonalInfo:

    def __init__(self, firstname, lastname, company, mobile_number):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.mobile_number = mobile_number

    def __str__(self):
        return (f"First Name: {self.firstname}, Last Name: {self.lastname}, Company: {self.company}, "
                f"Mobile Number: {self.mobile_number}")
