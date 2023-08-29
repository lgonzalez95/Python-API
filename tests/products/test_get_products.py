import logging as logger

import pytest

from src.helpers.ProductsHelper import ProductsHelper
from src.json_schemas import ProductSchemas
from src.utilities.AssertionUtility import assert_status_code, assert_expected_body_response_schema


@pytest.mark.products
def test_get_products_filtered():
    logger.info("TEST: get products based on a filter key word")
    expected_category_for_products = "Dress"
    products_obj = ProductsHelper()
    response = products_obj.get_products_filtered("dress")
    products_returned = response.json()["products"]
    assert_status_code(response, 200)
    assert_expected_body_response_schema(response, ProductSchemas.get_products_filtered_schema())
    for x in products_returned:
        assert expected_category_for_products == x["category"]["category"]


@pytest.mark.products
def test_get_products_filtered_fail_missing_search_key():
    logger.info("TEST: get products based on a filter key word")
    products_obj = ProductsHelper()
    response = products_obj.get_products_filtered()
    assert_status_code(response, 200)
    assert_expected_body_response_schema(response, ProductSchemas.get_products_filtered_missing_search_key_schema())