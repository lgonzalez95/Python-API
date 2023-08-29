import logging

from src.utilities.RequestsUtility import RequestUtility


class UsersHelper(object):
    def __init__(self):
        self.request_utility = RequestUtility()

    def create_user(self, personal_info, account_info, address_info):
        payload = {}
        instances = [personal_info, account_info, address_info]
        for instance in instances:
            for attr_name, attr_value in vars(instance).items():
                payload[f"{attr_name}"] = attr_value
        response = self.request_utility.post("/createAccount", payload)
        logging.debug(f"Received the following response: {response.json()}")
        return response

    def get_user(self, email):
        params = {
            "email": email
        }
        response = self.request_utility.get(endpoint="/getUserDetailByEmail", params=params)
        logging.debug(f"Received the following response: {response.json()}")
        return response

    def update_user(self, personal_info, account_info, address_info):
        payload = {}
        instances = [personal_info, account_info, address_info]
        for instance in instances:
            for attr_name, attr_value in vars(instance).items():
                payload[f"{attr_name}"] = attr_value
        response = self.request_utility.put("/updateAccount", payload)
        logging.debug(f"Received the following response: {response.json()}")
        return response
