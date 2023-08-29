import pytest

import logging as logger
from src.helpers.UsersHelper import UsersHelper
from src.json_schemas import UserSchemas
from src.utilities.DataFaker import get_random_personal_info, get_random_account_info, get_random_address_info
from src.utilities.AssertionUtility import assert_status_code, assert_expected_body_response_schema


@pytest.mark.users
@pytest.mark.tc_11
def test_update_user_valid_data():
    logger.info("TEST: update existing user with valid data.")
    personal_info = get_random_personal_info()
    account_info = get_random_account_info()
    address_info = get_random_address_info()
    updated_personal_info = get_random_personal_info()
    updated_account_info = get_random_account_info()
    updated_address_info = get_random_address_info()
    updated_account_info.email = account_info.email
    updated_account_info.password = account_info.password

    user_obj = UsersHelper()
    user_obj.create_user(personal_info, account_info, address_info)
    get_user_before_update = user_obj.get_user(account_info.email)
    update_response = user_obj.update_user(updated_personal_info, updated_account_info, updated_address_info)
    get_user_after_update = user_obj.get_user(account_info.email)

    assert_status_code(update_response, 200)
    assert_expected_body_response_schema(update_response, UserSchemas.update_user_schema())
    assert get_user_before_update.json() != get_user_after_update.json()
