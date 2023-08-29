class AddressInfo:
    def __init__(self, address1, address2, country, state, city, zipcode):
        self.address1 = address1
        self.address2 = address2
        self.country = country
        self.state = state
        self.city = city
        self.zipcode = zipcode

    def __str__(self):
        return (f"Address Line 1: {self.address2}, Address Line 2: {self.address2}, "
                f"Country: {self.country}, State: {self.state}, City: {self.city}, Zip Code: {self.zipcode}")
