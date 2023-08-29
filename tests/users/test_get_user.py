import logging as logger

import pytest

from src.dao.ProductsDAO import ProductsDAO
from src.helpers.UsersHelper import UsersHelper
from src.json_schemas import UserSchemas
from src.utilities.AssertionUtility import assert_status_code, assert_expected_body_response_schema


@pytest.mark.users
@pytest.mark.tc_14
def test_get_existing_user():
    logger.info("TEST: get an existing user using a valid email")
    email = "martinsalazar@example.com"
    user_obj = UsersHelper()
    response = user_obj.get_user(email)
    assert_status_code(response, 200)
    assert_expected_body_response_schema(response, UserSchemas.get_user_schema())


@pytest.mark.tc_100
def test_get_existing_user():
    logger.info("Getting from DB")
    data = ProductsDAO().get_all_products()
    for x in data:
        logger.error(x)
