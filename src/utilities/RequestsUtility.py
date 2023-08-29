import logging
import os

import requests

from src.config.Configuration import configuration


class RequestUtility(object):
    def __init__(self):
        self.env = os.environ.get("ENV", "local")
        self.base_url = configuration.base_api_url

    def post(self, endpoint, payload=None, headers=None):
        logging.debug(f"Sending post request using the payload: {payload}")
        url = self.base_url + endpoint
        if not headers:
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(url=url, data=payload, headers=headers)
        return response

    def get(self, endpoint, payload=None, headers=None, params=None):
        logging.debug(f"Sending get request using the payload: {payload}")
        url = self.base_url + endpoint
        if not headers:
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.get(url=url, data=payload, headers=headers, params=params)
        return response

    def put(self, endpoint, payload=None, headers=None):
        logging.debug(f"Sending put request using the payload: {payload}")
        url = self.base_url + endpoint
        if not headers:
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.put(url=url, data=payload, headers=headers)
        return response
