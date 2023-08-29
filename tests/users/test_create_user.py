import pytest

import logging as logger
from src.helpers.UsersHelper import UsersHelper
from src.json_schemas import UserSchemas
from src.utilities.DataFaker import get_random_personal_info, get_random_account_info, get_random_address_info
from src.utilities.AssertionUtility import assert_status_code, assert_expected_body_response_schema


@pytest.mark.users
@pytest.mark.tc_11
def test_create_user_valid_data():
    logger.info("TEST: Create a new user with valid data.")
    personal_info = get_random_personal_info()
    account_info = get_random_account_info()
    address_info = get_random_address_info()
    user_obj = UsersHelper()
    response = user_obj.create_user(personal_info, account_info, address_info)
    assert_status_code(response, 200)
    assert_expected_body_response_schema(response, UserSchemas.create_user_schema())


@pytest.mark.users
@pytest.mark.tc_15
def test_create_user_fail_for_existing_email():
    logger.info("TEST: Create a new user with valid data.")
    personal_info = get_random_personal_info()
    account_info = get_random_account_info(email="martinsalazar@example.com")
    address_info = get_random_address_info()
    user_obj = UsersHelper()
    response = user_obj.create_user(personal_info, account_info, address_info)
    assert_status_code(response, 200)
    assert_expected_body_response_schema(response, UserSchemas.create_user_fail_existing_email())
