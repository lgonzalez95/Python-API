def get_products_filtered_schema():
    return {
        "type": "object",
        "properties": {
            "responseCode": {"type": "integer", "const": 200},
            "products": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"},
                        "price": {"type": "string"},
                        "brand": {"type": "string"},
                        "category": {
                            "type": "object",
                            "properties": {
                                "usertype": {
                                    "type": "object",
                                    "properties": {
                                        "usertype": {"type": "string"}
                                    }
                                },
                                "category": {"type": "string"}
                            }
                        }
                    },
                    "required": ["id", "name", "price", "brand", "category"]
                }
            }
        },
        "required": ["responseCode", "products"]
    }


def get_products_filtered_missing_search_key_schema():
    return {
        "type": "object",
        "properties": {
            "responseCode": {"type": "integer", "const": 400},
            "message": {"type": "string", "const": "Bad request, search_product parameter is missing in POST request."}
        },
        "required": ["responseCode", "message"]
    }
