#HTTP Status Verification

def verify_http_status_code(response, expect_data):
    assert response.status_code == expect_data, "Expected HTTP status code"+str(expect_data)


def verify_json_key_for_not_null(key):
    assert key != 0, "key is not empty "+key
    assert key > 0 , "key is greater than 0"


def verify_json_key_for_not_none(key):
    assert key is not None

def verify_response_time():
    pass