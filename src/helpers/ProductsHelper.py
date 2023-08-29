import logging as logger

from src.utilities.RequestsUtility import RequestUtility


class ProductsHelper(object):
    def __init__(self):
        self.request_utility = RequestUtility()

    def get_products_filtered(self, filter_key=None):
        logger.debug(f"Sending post request to get products using the key: {filter_key}")
        payload = {"search_product": filter_key}
        response = self.request_utility.post("/searchProduct", payload)
        logger.debug(f"Received the following response: {response.json()}")
        return response
