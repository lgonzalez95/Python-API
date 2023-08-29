def get_user_schema():
    return {
        "type": "object",
        "properties": {
            "responseCode": {"type": "integer"},
            "user": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "email": {"type": "string", "format": "email"}
                },
                "required": ["id", "email"]
            }
        },
        "required": ["responseCode", "user"]
    }


def create_user_schema():
    return {
        "type": "object",
        "properties": {
            "responseCode": {"type": "integer", "const": 201},
            "message": {"type": "string", "enum": ["User created!"]}
        },
        "required": ["responseCode", "message"]
    }


def create_user_fail_existing_email():
    return {
        "type": "object",
        "properties": {
            "responseCode": {"type": "integer", "const": 400},
            "message": {"type": "string", "const": "Email already exists!"}
        },
        "required": ["responseCode", "message"]
    }


def update_user_schema():
    return {
        "type": "object",
        "properties": {
            "responseCode": {"type": "integer", "const": 200},
            "message": {"type": "string", "const": "User updated!"}
        },
        "required": ["responseCode", "message"]
    }
