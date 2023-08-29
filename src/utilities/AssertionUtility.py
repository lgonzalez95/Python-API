import logging
import json
import jsonschema
from jsonschema import validate


def assert_status_code(response, expected_code):
    assert response.status_code == expected_code, f"An unexpected status code was received.\n" \
                                                  f"Expected: {expected_code}, but {response.status_code} was received.\n" \
                                                  f"URL: {response.request.url}\n" \
                                                  f"Request body: {response.request.body}\n" \
                                                  f"Request headers: {response.request.headers}"


def assert_expected_body_response_schema(response, response_schema):
    try:
        response_data = response.json()
        validate(instance=response_data, schema=response_schema)
        message = "Response data is valid"
    except jsonschema.exceptions.ValidationError as e:
        expected_value = e.validator_value[0] if type(e.validator_value) is list else e.validator_value
        expected_msg = f"\"{e.path[0]}\" property to be \"{expected_value}\""
        actual_msg = f"\"{e.instance}\""
        message = e.message
    assert message == "Response data is valid", f"An unexpected status code was received.\n" \
                                                f"Expected: {expected_msg}, but {actual_msg} was received.\n"
